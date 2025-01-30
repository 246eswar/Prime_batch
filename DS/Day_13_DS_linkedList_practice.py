#linked list
class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
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
l.display()




