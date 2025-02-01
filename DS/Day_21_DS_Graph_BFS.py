#Graph _BFS with Queue
#every node would visit one time only

#Theory part

#take 2 empty queues
Queue1={}
Queue2={}
#first step
#first level append in Queue1
Queue1={A}
Queue2={}
#step 2
#delete queue1 elements and at the same time append in the queue2
#adding connecting elements of A
Queue1={B,D}
Queue2={A}
