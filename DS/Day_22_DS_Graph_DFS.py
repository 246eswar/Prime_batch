#graph DFS
#see in paint for graph

#step1:
#push H on to the stack
STACK:H
#step2
STACK:A
#POP H from the STACK
print:H
#step3
STACK:B,D#LAST IN First Out
print: H,A
#step4
STACK:B,F
print: H,A,D
#step5
STACK:B
print: H,A,D,F
#step6
STACK:C
print: H,A,D,F,B
#step7
STACK:E,G
print: H,A,D,F,B,C
#step8
STACK:E
print: H,A,D,F,B,C,G
#step9
STACK:
print: H,A,D,F,B,C,G,E
