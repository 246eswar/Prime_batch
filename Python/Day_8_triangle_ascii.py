#number triangle:
n=int(input("Enter the valur: "))
for i in range(1,n+1):
    for j in range(i):
        print(str(i),end=" ")
    print()

n=int(input("Enter the valur: "))
for i in range(1,n+1):
    for j in range(i):
        print('*',end="")
    print()
