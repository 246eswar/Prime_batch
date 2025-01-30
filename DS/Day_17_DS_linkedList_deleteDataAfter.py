#Linked List
#Deletion after data
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class singleLinkedList:
    def __init__ (self):
        self.head=None
    def delete_DataAfter(self,dataafter):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp.next is not None and temp.data is not dataafter:
            temp=temp.next
        if temp.next is not None:
            temp.next=temp.next.next
        elif temp.data is not dataafter:
            print("Node is not present in the list")
        else:
            print("Deletion not possible this is the last node")            
    def display(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="-->")
                temp=temp.next

l= singleLinkedList()
n = Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
l.display()
print()
l.delete_DataAfter(30)
print()
l.display()

