from matplotlib import pyplot as plt 

def takeUserInput(msg1,msg2):
    num1 = int(input(msg1))
    num2 = int(input(msg2))
    return num1, num2


def DDA():
    # input the two endpoints of the line segment
    x1 ,y1 = takeUserInput("Enter X1: ","Enter Y1: ")
    x2 ,y2 = takeUserInput("Enter X2: ","Enter Y2: ")
    
    # calculate the difference between the x and y cordinates of the endpoints
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # find maximum difference
    steps = max(dx,dy)
    xinc = dx/steps
    yinc = dy/steps
    
    # calculate the slope of the line as m = dy/dx
    m = dy/dx
     
    #set initial point of line as x1,y1
    x , y = float(x1) , float(y1)
    
    print(f"({round(x)}, {round(y)})")  # Round and print the initial point
    
    #loop through the x cordinates incrementing by one
    # calculate corresponding y-cordinate using y = y1 + m(x-x1)
    while x != x2 or y != y2:  # Iterate until reaching the endpoint
        x += xinc
        y += yinc
        print(f"({round(x)}, {round(y)})")

        
        
DDA()
            
    
    