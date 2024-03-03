initialNumber = 65
#To determine the position of the text
charIndex = 0 
for i in range(65,123):
    if charIndex % 2 == 0: 
        print(f"{chr(i + 32 )} => {i + 32}")
        charIndex += 1
        # print(charIndex)
    else:
        print(f"{chr(i)} => {i}")
        charIndex += 1
        # print(charIndex)
        
    

