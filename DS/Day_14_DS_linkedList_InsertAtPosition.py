#InsertAt pisition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_position(self,position_value,data):
        new_position=Node(data)
        temp=self.head
        for i in range(position_value - 1):
            temp=temp.next
            new_position.data=data
            new_position.next=temp.next
            temp.next=new_position        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end="-->")
                temp=temp.next
l=sll()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(20)
n1.next=n2
n3=Node(20)
n2.next=n3
n4=Node(20)
n3.next=n4
l.insert_position(2,50)

l.display()
