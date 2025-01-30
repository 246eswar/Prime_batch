#delete At_position

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        else:
            new_node.next = self.head  
            self.head = new_node  
            self.tail.next = self.head
    def insert_Position(self,position_value,data):
        newNode=Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        if position_value == 0:
            newNode.next=self.head
            current=self.head
            while current.next is not self.head:
                current=current.next
            current.next=newNode
            self.head=newNode
        current=self.head
        count=0
        while count < position_value -1 and current.next is not self.head:
            current=current.next
            count+=1
        newNode.next=current.next
        current.next=newNode
    def display(self):
        if self.head is None:
            print("Circular List is Empty")
        
        temp = self.head
        while True:
            print(temp.data, end="-->")
            temp = temp.next
            if temp == self.head:  
                    break
        print()  
l = cll()  
n = Node(10)
l.head = n
l.tail = n
l.tail.next = l.head  
print("First element")
l.display() 

print("Second element")
n1 = Node(20)
l.tail.next = n1  
l.tail = n1  
l.tail.next = l.head  
l.display()  
print("New node inserted at front")
l.insert_begin(5)  
l.display()
l.insert_begin(15)  
l.display()  

l.insert_Position(2,40)
l.display()


