#python inheritance
'''Inheritance allows us to define a class methods
and properties from another class'''
#base class -->main(parent) class
#derive class  -->child class

'''class Animal:
    def speak(self):
        return "Animals cannot speak"
class Cat(Animal):
    def drink(self):
        return "Cat Drinks Milk"
a=Cat()
print(a.drink())
print(a.speak())'''
    
class Animal:
    def speak(self):
        return "Animals cannot speak"
class Cat(Animal):
    def drink(self):
        return "Cat Drinks Milk"
a=Animal()
print(a.speak())
print(a.drink())
