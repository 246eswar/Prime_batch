'''create a class with the name of calculator and
perform +,-,*,/ as a method and call the all four operations'''
#check once code is not cot complete
class calculator:
    a=int(input("first number: "))
    b=int(input("second number: "))
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
a=int(input("first number: "))
b=int(input("second number: "))
print(calculator.add(a,b))
print(calculator.sub(a,b))
print(calculator.mul(a,b))
print(calculator.div(a,b))
