#QUEUE -- using class
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class queue:
    def __init__ (self):
        self.front=None
        self.rear=None
    def enqueue(self):
        data=int(input("Enter the data: "))
        newNode=Node(data)
        if self.front==None:
            self.front=newNode
            self.rear=newNode
            print(data,"is added to queue")
        else:
            self.rear.next=newNode
            self.rear=newNode
            print(data,"is added to queue")
    def dequeue(self):
        if self.front==None:
            print("QUEUE is empty")
        elif self.front.next == None:
            print("popped element:",self.front.data)
            self.front=None
            self.rear=None
        else:
            temp=self.front
            print("Popped element is:",self.front.data)
            self.front=temp.next
            temp=None
    def display(self):
        if self.front==None:
            print("QUEUE is empty")
        else:
            print("element of the queue are:")
            temp=self.front
            while temp:
                print(temp.data)
                temp=temp.next
            print("\n front:",self.front.data)
            print("\n rear:",self.rear.data)
Q=queue()
while(1):
    print("Enter the option from below: \n1-Enqueue Operation \n2-Dequeue Operation \n3-Display")
    option=int(input())
    if option == 1:
        print("ENQUEUE OPERATION")
        Q.enqueue()
    elif option == 2:
        print("DEQUEUE OPERATION")
        Q.dequeue()
    elif option == 3:
        print("DISPLAY OPERATION")
        Q.display()
    else:
        print("print valid Option")
        break


            
