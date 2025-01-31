#fixed circular Queue 
class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def full(self):
        return self.front == (self.rear + 1 ) % self.size
        #or return self.rear +1 == self.size and self.front == 0
        #or self.rear+1 == self.front
    def empty(self):
        return self.front == -1
    def enqueue(self,item):
        if self.full():
            print("Circular Queue is full")
        if self.empty():
            self.front=0
        if self.rear+1 == self.size:
            self.rear = 0
        else:
            self.rear += 1
            #or self.rear = (self.rear + 1 ) % self.size
        self.queue[self.rear]=item
        print(f"enqueue: {item}")
    def dequeue(self):
        if self.empty():
            print("Queue is empty")
        #front is increment
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front=self.rear=-1
        if self.front +1 == self.size:
            self.rear = 0
        else:
            self.front += 1
        print("Dequeue: ",item)
        return item
    def peek(self):
        if self.empty():
            print("Queue is empty")
        return self.front.item
    def display(self):
        if self.empty():
            print("Queue is EMPTY")
            return
        #chack front and rear position
        if self.rear >= self.front:
            print("Queue elements are: ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        #1st loop front to max size
        print("Queue elements are: ")
        for i in range(self.front,self.size):
            print(self.queue[i],end=" ")
            #2 is start from 0 to rear
        for j in range(0,self.rear+1):
            print(self.queue[j],end=" ")
cq=CircularQueue(5)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)
cq.display()
