class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message

# Example usage
cipher = CaesarCipher(shift=3)
message = "Hello, Bernard!"
encrypted_message = cipher.encrypt(message)
decrypted_message = cipher.decrypt(encrypted_message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
