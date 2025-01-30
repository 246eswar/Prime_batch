#method Overloading
'''Overloading is a method or operator that can do
different functionalities with the same name
Methods in python can be called with zero,or more
parameters.This process of calling the same method
in different ways called method overloading'''
#overriding is based on two classes
#overloading is on one class
'''class mathoperation:
    def add(self,a,b=5,c=20):#1.default argument
        return a+b+c
math=mathoperation()
print(math.add(20))
print(math.add(10,20))
print(math.add(10,20,30))'''
    
'''class mathoperation:
    def add(self,*args):#2.variable length argument
        return sum(args)
math=mathoperation()
print(math.add(20))
print(math.add(10,20))
print(math.add(10,20,30))'''

#POLYMORPHISM
'''one in many forms
#perticular functionality it can be done by many forms'''
class mathoperation:
    def add(self,*args):#2.variable length argument
        return max(args)
math=mathoperation()
print(math.add(20))
print(math.add(10,20))
print(math.add(10,20,30))
