'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print("",end=" ")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(i-1,0,-1):
        print(l,end="")
    print()'''
n=4
num=1
for i in range(n):
    for j in range(n-i-1):
        print(""*(n-i),end=" ")
    for k in range(2*i-1):
        print(num,end="")
        num+=1
    print()
