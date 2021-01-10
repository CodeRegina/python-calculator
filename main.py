import re 

print("Python Calculator is Snaketastical")
print("Type 'quit' to exit\n")


previous = 0
run = True 

def performMath():
    global run 
    global previous 
    num = ""
    if previous == 0:
        num = input("Enter: ")
    else:
        num = input(str(previous))

    if num == 'quit':
        print("Thanks for using Snaketastical Calculator. ")
        run = False 

    else:
        num = re.sub('[a-zA-Z,.:()" "]', '', num)
    if previous == 0:
        previous = eval(num)
    else:
            previous = eval(str(previous) + num)

    performMath() 
