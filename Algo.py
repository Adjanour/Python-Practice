def takeUserInput(msg1,msg2):
    num1 = int(input(msg1))
    num2 = int(input(msg2))
    return num1, num2

def dda_line():
    # input the two endpoints of the line segment
    x1 ,y1 = takeUserInput("Enter X1: ","Enter Y1: ")
    x2 ,y2 = takeUserInput("Enter X2: ","Enter Y2: ")
    length = int(input("How many steps do you want: "))
    
    dx = x2 - x1
    dy = y2 - y1

    slope = dy / dx if abs(dx) > abs(dy) else dx / dy  # Handle slopes > 1 and < 1

    if abs(slope) < 1:
        step_x = 1
        step_y = slope * step_x
    else:
        step_y = 1
        step_x = slope * step_y 

    x = x1
    y = y1

    
    i = 0
    while True:
        i += 1
        if i == length:
            break
        x += step_x
        y += step_y
        
        
        print(f"({x},{y})")
        print(f"({round(x)},{round(y)})\n")

    
dda_line()
