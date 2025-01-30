class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insertAtFront(self, data):
        newNode = Node(data)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head  # Point to itself
        else:
            newNode.next = self.head
            self.tail.next = newNode  # Point the old tail to the new node
            self.head = newNode  # Update head to new node

    def display(self):
        if self.isEmpty():
            print("List is empty")
            return
        
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

cll = CircularLinkedList()
n = int(input("Enter how many elements you would like to add: "))
    
for _ in range(n):
    data = int(input("Enter data element: "))
    cll.insertAtFront(data)
    print("Adding nodes to the start of the list:")
    cll.display()
