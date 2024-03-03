def get_user_input(message1, message2, message3):
    a = input(message1)
    b = input(message2)
    c = input(message3)
    
    return a, b, c

def AND():
    first, second, third = get_user_input("Enter first input: ", "Enter second input: ", "Enter third input: ")
    return first and second and third

def OR():
    first, second, third = get_user_input("Enter first input: ", "Enter second input: ", "Enter third input: ")
    return first or second or third

def NOT():
    user_input = input("Enter input: ")
    return not user_input

def implication():
    first, second = get_user_input("Enter first input: ", "Enter second input: ", "")
    return (not first) or second

def biconditional():
    first, second = get_user_input("Enter first input: ", "Enter second input: ", "")
    return (first and second) or ((not first) and (not second))

def conditional():
    first, second = get_user_input("Enter first input: ", "Enter second input: ", "")
    return (not first) or second


def main():
    print("Welcome")
    print(""" 
          1.Conditional
          2.Implication
          3.NOT
          4.AND
          5.Biconditional
          6.OR
          """)
    user_input = get_user_input("What are you doing today: ","","")
    if user_input == 1:
        print(conditional())
        
        

# if "name" == main :
#     main()

main()