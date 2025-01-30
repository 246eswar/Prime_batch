def enqueue():
    n = int(input("Enter the element to be inserted:"))
    queue.append(n)
    print(n,"is added to queue")
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue[0],"is the element to be deleted")
        queue.pop(0)# (or)  del queue[0]
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Elements in the queue are: ")
        for i in queue:
            print(i)
        print("Front:",queue[0])
        print("Rear:",queue[-1])
queue = list()
while(1):
    print("Enter the option from below: \n1-Enqueue Operation \n2-Dequeue Operation \n3-Display")
    option=int(input())
    if option == 1:
        print("ENQUEUE OPERATION")
        enqueue()
    elif option == 2:
        print("DEQUEUE OPERATION")
        dequeue()
    elif option == 3:
        print("DISPLAY OPERATION")
        display()
    else:
        print("print valid Option")
        break
