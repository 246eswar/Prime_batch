'''n=5
num=1
for i in range(n):
    for j in range(1,i+1) :
        print(num,end=" ")
        num+=1
    for k in range(i-1,0,-1):
        print(num,end=" ")
        num+=1
    print()'''

n=10
for i in range(n):
    for j in range(n-1-i) :
        print("",end=" ")
    for k in range(1,i+1):
        print(chr(64+k),end="")       
    for l in range(i-1,0,-1):
        print(chr(64+l),end="")
    print()
