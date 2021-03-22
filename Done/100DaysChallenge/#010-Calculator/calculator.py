import art
import os

print(art.logo)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation_dict = {"+":add,
                  "-":subtract,
                  "*":multiply,
                  "/":divide}

function = None
result = 0

while True:
    
    
    if function:
        num1 = result
    else:
        num1 = float(input("What's the 1st number? "))
    

    function = None    
    while function not in operation_dict.keys():
        function = input("Choose operation:\n"
                        "+ for sum\n"
                        "- for substract\n"
                        "* for multiply\n"
                        "/ for divide\n"
                        )
        
    num2 = float(input("What's the 2nd number? "))
    result = operation_dict[function](num1,num2)
    print("------------")
    print(f"{num1} {function} {num2} = {result}")
    print("------------")
    
    _continue = input("Do you want to continue calculation?\n"
                      "'y' for yes\n"
                      "'n' for new\n"
                      "any other key to exit ").lower()
    if _continue[0] == 'n':
        function = None
        os.system('cls')
        print(art.logo)
    elif _continue[0] != 'y':
        break
    else:
        os.system('cls')
        print(art.logo)
        print(f"Num1: {result}")

