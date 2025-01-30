max_size = 5
queue=[]
def enqueue(queue,max_size,data):
    
    if len(queue) >= max_size:
        print("full")
    else:
        queue.append(data)
        print(data,"is the element to be deleted")
def dequeue(queue):
    if len(queue) == 0:
        print("Empty")
    else:
        data=queue.pop(0)
        print(data,"is the element to be deleted")
def display(queue):
    if len(queue) == 0:
        print("QUEUE is EMPTY")
    else:
        print("Elements in the queue are: ")
        print("Front:",queue[0])
        print("Rear:",queue[-1])
while True:
    print("Enter: ")
    op=int(input())
    if op==1:
        ele=int(input("Enter the element to be inserted: "))
        enqueue(queue,max_size,ele)
    elif op==2:
        dequeue(queue)
    elif op == 3:
        display(queue)
    else:
        break
