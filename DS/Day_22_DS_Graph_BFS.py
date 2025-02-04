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
#adding connecting elements of A and check no repeatations
Queue1={B,D}
Queue2={A}
#step3
#repeate step 2
Queue1={D,C,F}
Queue2={A,B}
#step4
#repeate step 2
Queue1={C,F}
Queue2={A,B,D}
#step5
#repeate step 2
Queue1={F,E,G}
Queue2={A,B,D,C}
#step6
#repeate step 2
Queue1={}
Queue2={A,B,D,C,F,E,G}
'''#step7
#repeate step 2
Queue1={G}
Queue2={A,B,D,C,F,E}
#step8
#repeate step 2
Queue1={}
Queue2={A,B,D,C,F,G}'''
FINALLY:
    A,B,D,C,F,E,G

