#Linked List
#DeletionAtEnd
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class singleLinkedList:
    def __init__ (self):
        self.head=None
    #temp and prev both are taken
    #temp is deleted(i.e.,if temp.next is None)
    #prev.next is temp that is None
    def delete_At_End(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            if temp.next is None:
                self.head=None
                return
            prev=None
            while temp.next is not None:
                prev=temp
                temp=temp.next
        prev.next=None            
    def display(self):
        if self.head == None:
            print("Nothing to display")
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
l.delete_At_End()
print()
l.display()

