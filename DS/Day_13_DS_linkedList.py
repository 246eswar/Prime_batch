#Linked List

#Node create means create first class
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None#address not required while initial
        #if next=None initially we can pass next above or remove next
        #if fixed then include another way of empty next are below
        #self.next=False
        #self.next=0
        #self.next=[]
class singleLinkedList:
    def __init__ (self):
        self.head=None#initial Node is empty Head
        #for visiual list print statement and ue loop for linked and addresses
        #display method
    def display(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            temp = self.head#head is fixed so assign to variable
            while temp:
                print(temp.data,end="-->")#end= for link visiual
                temp=temp.next
#two objects
#one is for head for temp using
#another for data
l= singleLinkedList()
n = Node(10)#data
l.head=n#head goes to next node
n1=Node(20)#data
n.next=n1#connection
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
l.display()

