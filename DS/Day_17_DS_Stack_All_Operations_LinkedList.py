#stack using Linked list
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None#first position
    def push(self):
        data=int(input("Enter element to be inserted into the stack: "))
        newNode=Node(data)
        #self.top.next=None
        if self.top is None:
            self.top=newNode
            self.top.next=None
        else:
            newNode.next=self.top
            self.top=newNode
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("popped data is:",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("popped data is:",self.top.data)
            self.top=temp.next
            temp=None
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(self.top.data)
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Elements of the stack are :")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("Top of the list is:",self.top.data)
s=stack()
while(1):
    print("Enter the options from below")
    print("1.Push \n","2.Pop \n","3.peek \n","4.display")
    option=input("Enter the which operation is to be performed: ")
    if option == '1':
        s.push()
    elif option == '2':
        s.pop()
    elif option == '3':
        s.peek()
    elif option == '4':
        s.display()
    else:
        print("Exit the program")
        break
    
