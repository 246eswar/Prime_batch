#Queue
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)
queue.append(9)
f=queue.pop(0)
print(f)
print(queue)#after pop 1st element
is_empty=len(queue) == 0
size = len(queue)
print(is_empty)
print(size)
