#super keyword  --> it uses to print both parent and child data in method overriding

class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        parent_speak = super().speak()
        #super function dot speak method
        return f"{parent_speak} and Dog barks"
a=Dog()
print(a.speak())
