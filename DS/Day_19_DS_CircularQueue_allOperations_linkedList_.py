#circular queue using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CQ:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_Empty(self):
        return self.front is None
    def enqueue(self,item):
        newNode=Node(item)
        if self.is_Empty():
            self.front=newNode
            self.rear=newNode
            newNode.next=self.front
        else:
            self.rear.next=newNode
            self.rear=newNode
            self.rear.next=self.front
        print("enqueue:",item)
    def dequeue(self):
        if self.is_Empty():
             print("Empty")
        temp= self.front.data
        if self.front == self.rear:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front
        print("Dequeue:",temp)
    def peek(self):
        if self.is_Empty():
             print("Empty")
        return self.front.data
    def display(self):
        if self.is_Empty():
             print("Empty")
        #itterarion
        temp=self.front
        while True:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.front:
                break
        print()
l = CQ()
l.enqueue(10)
l.display()
l.enqueue(10)
l.display()
l.dequeue()    
l.display()    
                
