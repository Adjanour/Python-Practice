import ImprovedEuclideanAlgorithm as ie

# Take the input from the user
numbers = ie.takeUserInput(5)

# Compute the GCD of the numbers in the list
gcd = ie.improvedEuclideanAlgorithm(*numbers)

# Print the result
print(f"The GCD of the numbers {numbers} is {gcd}")