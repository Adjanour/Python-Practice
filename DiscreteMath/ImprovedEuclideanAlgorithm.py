import EuclideanAlgorithm as e
def takeUserInput(numOfInputs):
    """Takes user input for the number of numbers specified in the argument list.

    Args:
        *numOfInputs (int): number of numbers to take input for

    Returns:
        list : list of numbers
    """
    numbers = []
    for i in range(numOfInputs):
        numbers.append(int(input(f"Enter number {i+1}: ")))
    return numbers

def improvedEuclideanAlgorithm(*numbers)->int:
    """Computes the greatest common divisor of a list of numbers using the Euclidean Algorithm.

    Args:
        *numbers (int): list of numbers

    Returns:
        int : greatest common divisor of the numbers
    """
    #sort the numbers in ascending order
    numbers = sorted(numbers)
    #compute the greatest common divisor of the first two numbers
    gcd = e.euclideanAlgorithm(numbers[0], numbers[1])
    #compute the greatest common divisor of the remaining numbers
    for i in range(2, len(numbers)):
        gcd = e.euclideanAlgorithm(gcd, numbers[i])
    return gcd