#Stack
class stack:
    def __init__(self):
        self.items=[]#Empty
    def push(self,item):#data need to push
        self.items.append(item)
        print( self.items)
    def pop(self):
        if len(self.items)==0:
            raise IndexError("POP from an empty stack")
        return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack item from top to bottom:")
            #top to bottom means reverse #bottom to top is normal
            for i in reversed(self.items):
                print(i)
s=stack()
'''
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.push(60)
s.display()'''
while(1):
    print("Enter the operation")
    print("1-->push operation")
    print("2-->pop operation")
    print("3-->peek operation")
    print("4-->size operation")
    print("5-->is_empty")
    print("6-->display")
    option=input()
    if option=='1':        
        print("push operation")
        s.push(10)
    elif option=='2':        
        print("pop operation")
        s.pop()
    elif option=='3':        
        print("peek operation")
        s.peek()
    elif option=='4':        
        print("size operation")
        s.size()
    elif option=='5':        
        print("is_empty")
        s.is_empty()
    elif option=='6':
        print("display")
        s.display()
    else:
        print("Exit the program")
        break
    
