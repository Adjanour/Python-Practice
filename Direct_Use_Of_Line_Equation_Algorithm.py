def takeUserInput(msg1,msg2):
    num1 = int(input(msg1))
    num2 = int(input(msg2))
    return num1, num2

def algo():
    
    x1,y1 = takeUserInput("Enter x1: ","Enter : ")
    x2,y2 = takeUserInput("Enter x2: ","Enter y2: ")
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    b = y1 - (m*x1)
    while (True):
        if dx < 0:
            x = x2
            y = y2
            xend = x1
        if dx > 0:
            x = x1
            y = y1
            xend = x2
        
        if x == xend:
            break
        
        print(f"({x},{y})")
        x = x +1
        y = (m*x) +b
    
algo()