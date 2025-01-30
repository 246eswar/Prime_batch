'''insert beginning'''
#insert at position
#insert at Last
#linked list
class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=node(data)
        #new node is taken from Node class
        new_node.next=self.head
        self.head=new_node        
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end='-->')
                temp=temp.next
l=sll()
n=node(10)
l.head=n
n1=node(20)
n.next=n1
l.insert_begin(30)
l.display()
print()
l.insert_begin(40)
l.display()
print()
l.insert_begin(50)
l.display()

