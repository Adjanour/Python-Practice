class CPU:
    def __init__(self):
        self.memory = [0] * 256  # 256 bytes of memory
        self.registers = [0] * 8  # 8 general-purpose registers
        self.pc = 0  # Program Counter

    def load_program(self, program):
        for i, instruction in enumerate(program):
            self.memory[i] = instruction

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode(self, instruction):
        opcode = instruction >> 5
        operand = instruction & 0b1111
        return opcode, operand

    def execute(self, opcode, operand):
        if opcode == 0b000:  # NOP
            pass
        elif opcode == 0b001:  # LOAD
            self.registers[0] = self.memory[operand]
        elif opcode == 0b010:  # STORE
            self.memory[operand] = self.registers[0]
        elif opcode == 0b011:  # ADD
            self.registers[0] += self.memory[operand]
        elif opcode == 0b100:  # SUB
            self.registers[0] -= self.memory[operand]
        elif opcode == 0b101:  # JUMP
            self.pc = operand
        elif opcode == 0b110:  # JUMP IF ZERO
            if self.registers[0] == 0:
                self.pc = operand
        elif opcode == 0b111:  # HALT
            print("HALT")
            return True  # Halt the CPU

        return False  # Continue execution

    def run(self):
        halt = False
        while not halt:
            instruction = self.fetch()
            opcode, operand = self.decode(instruction)
            halt = self.execute(opcode, operand)


# Example program
# Program to add two numbers: 5 + 7
program = [
    0b00100010,  # LOAD value 5 into register 0
    5,           # Value to load
    0b01000011,  # STORE value from register 0 into memory location 3
    3,           # Memory location
    0b00100011,  # LOAD value 7 into register 0
    7,           # Value to load
    0b01100011,  # ADD value from memory location 3 to register 0
    3,           # Memory location
    0b01000000,  # STORE result from register 0 into memory location 0
    0,           # Memory location to store result
    0b11100000   # HALT
]

# Initialize and run the CPU
cpu = CPU()
cpu.load_program(program)
cpu.run()

# Retrieve and print the result from register 0
result = cpu.registers[0]
print("Result:", result)
print("Memory:", cpu.memory)
