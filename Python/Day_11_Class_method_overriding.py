#Method Overriding
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
cat=Cat()
dog=Dog()
print(cat.speak())
print(dog.speak())
        
