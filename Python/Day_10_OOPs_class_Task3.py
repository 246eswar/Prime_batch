#constructor
'''
__init__ -->default constructor of a class
'''
#option based function call

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
#choice
#whileloop
choice =1 #1 is True
while choice!=0:#it itterate upto choice=0
    print("0.Exit")#condition if false Exit
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter Choice: "))
    if choice == 1:
        obj.add()
    elif choice == 2:
        obj.sub()
    elif choice == 3:
        obj.mul()
    elif choice == 4:
        obj.div()
    elif choice == 0:
        print("Exiting!!!")
    else:
        print("invalid choice...")

        
    
    
