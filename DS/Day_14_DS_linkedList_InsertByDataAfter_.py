
#dataafter
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def afterdata(self,dataafter,data):
        new=Node(data)
        temp=self.head
        while temp.next is not None and temp.data is not dataafter:
            temp=temp.next
        if temp.next is not None:
            new.next=temp.next
            temp.next=new
            return
        elif temp.data is not dataafter:
            print("node is not present")
            return
        else:
            new.next=None
            temp.next=new          
        
    def display(self):
        if self.head is None:
            print("sll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="")
                temp=temp.next
l=sll()
n=Node(45)
l.head=n
n1=Node(55)
n.next=n1
n2=Node(46)
n1.next=n2
l.display()
print()
l.afterdata(45,34)
l.display()
        
