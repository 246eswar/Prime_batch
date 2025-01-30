#Linked List
#DeletionAtPosition
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class singleLinkedList:
    def __init__ (self):
        self.head=None
    def delete_At_Position(self,position_value):
        if self.head is None:
            print("List is empty")
            return
        prev=self.head
        temp=self.head
        while temp.data is None and temp.data is not temp.dataafter:
            prev=temp
            temp=temp.next
        if temp.next is None:
            print("not found")
        else:
            
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
l.delete_At_Position(3)
print()
l.display()

