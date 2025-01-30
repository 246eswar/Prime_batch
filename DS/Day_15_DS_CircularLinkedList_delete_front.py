#delete front

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
            self.tail.next = self.head  # Circular link
        else:
            new_node.next = self.head  # New node points to head
            self.head = new_node  # Update head to the new node
            self.tail.next = self.head  # Tail's next should point to new head
    def delete_front(self):
        if self.head != self.tail:
            self.head=self.head.next
            self.tail.next=self.head
        else:
            self.head = None
            self.tail = None
    def display(self):
        if self.head is None:
            print("Circular List is Empty")
        
        temp = self.head
        while True:
            print(temp.data, end="-->")
            temp = temp.next
            if temp == self.head:  # Stop when we reach back to the head
                    break
        print()  # To move to the next line after displaying the list

# Testing the circular linked list operations
l = cll()  # Create circular linked list
n = Node(10)
l.head = n
l.tail = n
l.tail.next = l.head  # Circular link for single node
print("First element")
l.display()  # Output: 10-->10

print("Second element")
n1 = Node(20)
l.tail.next = n1  # Link the current tail to the new node
l.tail = n1  # Update the tail to the new node
l.tail.next = l.head  # Circular link back to the head
l.display()  # Output: 10-->20-->10

print("New node inserted at front")
l.insert_begin(5)  # Insert 5 at the beginning
l.display()  # Output: 5-->10-->20-->5

l.delete_front()
l.display()


