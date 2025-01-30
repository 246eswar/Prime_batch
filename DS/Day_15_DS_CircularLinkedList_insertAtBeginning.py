#circular linked list
#insert At Beginning

class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class cll:
    def __init__ (self):
        self.head=None
        self.tail=None

    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head#new_node link with head
            self.head=new_node#head go to first
            self.tail.next=self.head#tail and head link

        
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
print()
print("New_node insert at front")
l.insert_begin(5)
l.display()
