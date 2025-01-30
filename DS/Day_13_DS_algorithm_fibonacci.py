def fibb(n):
    #base case for recursion
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibb(n-1)+fibb(n-2)
def seq(n):
    li=[]
    for i in range(n+1):
        li.append(fibb(i))
    return li
n=int(input("n: "))
print(seq(n))
