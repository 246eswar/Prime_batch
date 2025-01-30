n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end="")
    print()
print()
n=5
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end="")
    print()
