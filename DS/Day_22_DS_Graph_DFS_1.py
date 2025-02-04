#graph DFS
#see in paint for graph

#step1:
#push A on to the stack
STACK:A
#step2
STACK:B,D
#POP A from the STACK
print:AP
#step3
STACK:B,F#LAST IN First Out
print: A,D
#step4
STACK:B
print: A,D,F
#step5
STACK:C
print: A,D,F,B
#step6
STACK:E,G,H
print: A,D,F,B,C
#step7
STACK:E,G
print: A,D,F,B,C,H
#step8
STACK:E
print: A,D,F,B,C,H,G
#step9
STACK:
print: A,D,F,B,C,H,G,E
