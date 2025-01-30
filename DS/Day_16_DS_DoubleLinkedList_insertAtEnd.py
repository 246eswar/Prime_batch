#Double Linked List_insert at beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__ (self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty__")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="<-->")
                temp=temp.next
    def insert_End(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
            newNode.prev=temp
l=DLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
l.display()
print()
n3=Node(30)
n2.next=n3
n3.prev=n2
l.display()
print()
n4=Node(40)
n3.next=n4
n4.prev=n3
n5=Node(50)
n4.next=n5
n5.prev=n4
l.display()
print()
l.insert_End(60)
l.display()

    
