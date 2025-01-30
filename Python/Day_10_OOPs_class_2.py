'''class Qis:
    name="Eswar"
    print("Hello QIS,we are back",name)
    def fun(name):
        print("Hello ",name)#usnig name in function        
a=Qis()#Object assign
Qis.fun("ravi")#function call
a.fun("ravi")#function call'''
'''self keyword refers to the current instance of the class
and accesses the class variables'''
#self is first argument
class Qis:
    name="Eswar"
    print("Hello QIS,we are back",name)
    def fun(self):
        print("Hello ",self.name)#usnig name in function        
a=Qis()#Object assign
#Qis.fun("ravi")#function call
a.fun()#object call

