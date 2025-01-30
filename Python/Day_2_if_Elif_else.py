a=float(input("Enter first number : "))
b=float(input("Enter second Number : "))

operator = input("Enter operator (+,-,/,*,%): ")    
if operator == '+':
    result=a+b
elif operator =='-':
    result=a-b
elif operator =='*':
    result=a*b
elif operator=='/':
    if b!=0:
        result=a/b
    else:
        result="Division by Zero is undefined"
elif operator=='%':
    result=a%b
else:
    result="Invalid Operator"
print(result)
