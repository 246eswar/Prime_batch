#constructor
'''
__init__ -->default constructor of a class
'''
class calculator:    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=calculator(a,b)
obj.add()
obj.sub()
obj.mul()
obj.div()
