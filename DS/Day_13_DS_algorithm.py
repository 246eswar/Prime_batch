#Data Structure
#data
#information
'''search
sort
add
delete
understand Alogorithm

properties of algorithm
input
output
definiteness
finiteness
effectiveness
correctiveness

(sudo code and normal code)'''
#define a function of factorial and function factorial
'''
Function factorial(n)
  IF n==0 THEN
    RETURN 1
  ELSE
    RETURN n*factorial(n-1)
END FUNCTION'''

def factorial(n):    
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("num: "))
print(factorial(n))












