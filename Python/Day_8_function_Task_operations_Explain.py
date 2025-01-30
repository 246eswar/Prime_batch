'''take a function the input should be given by the user
if input is +,-,*,/,& operation any two (+- then division)'''


def calculation():
    num1 = input("Enter the first number:")
    set1=set(num1)
    operation=input("Enter the operator: ")
    num2 = input("Enter the second number:")
    set2=set(num2)
    if operation == '+':
        result = int(num1)+int(num2)
        print(f"the result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = int(num1)-int(num2)
        print(f"the result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = int(num1)+int(num2)
        print(f"the result of {num1} * {num2} is: {result}")
    elif operation == '/':
         result = int(num1)/int(num2)
         print(f"the result of {num1} / {num2} is: {result}")       
    elif operation == '&':
        result = set1.intersection(set2)
        print(f"{set1} and {set2} is: {result}")
    elif operation == '|':
        result = set1.union(set2)
        print(f"{set1} and {set2} is: {result}")
    elif operation == '&':
        result = set1^set2
        print(f"{set1} and {set2} is: {result}")
    else:
        print("Enter correct operator")
calculation()
