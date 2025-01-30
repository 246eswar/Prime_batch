#circularLinkedList
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class cll:
    def __init__ (self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("Circle List is Empty")
        else:
            temp=self.head
            print(temp.data,end="-->")
            while temp.next!=self.head:                
                temp=temp.next
                print(temp.data,end="-->")
            
l=cll()#connection between classes
n=Node(10)
l.head=n
l.tail=n
#for single node head and tail are same
l.tail.next=l.head#for circle
print("first element")
l.display()
print()
print("second element")
n1=Node(20)
l.tail.next=n1#in circle base on links not nodes
l.tail=n1
l.tail.next=l.head
l.display()
