#recursion
#function inside a function

#void
def fact(n):
    if n==1:#base case
        return 1
    else:
        return n*fact(n-1)
n=int(input("n: "))
print(fact(n))

#fruitful
def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)
n=int(input("n: "))
print(fact(n))
            
        
