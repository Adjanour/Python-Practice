def takeUserInput():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return num1, num2


def euclideanAlgorithm(num1, num2)->int:
    """Computes the greatest common divisor of two numbers using the Euclidean Algorithm.

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int : greatest common divisor of num1 and num2
    """
    #check if num1 is greater than num2
    if num1 < num2: 
        num1, num2 = num2, num1
    while num2 != 0:
        remainder = num1 % num2
        print(f"{num1} / {num2} = {round((num1-remainder)/num2)} x {num2} + {remainder} ")
        num1 = num2
        num2 = remainder
    return num1

def main():
    num1, num2 = takeUserInput()
    print(f"The greatest common divisor of {num1} and {num2} is {euclideanAlgorithm(num1, num2)}")
    
if __name__ == "__main__":
    main()