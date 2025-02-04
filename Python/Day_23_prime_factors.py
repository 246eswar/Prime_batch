def sieve_of_E(n):
    #fixed size
    prime_or_not = [True]*(n+1)#initially all are taken True
    prime_or_not[0] = prime_or_not[1] = False #0&1 are not prime numbers
    for p in range(2,int(n**0.5)+1):
    #starting point is 2 and ending point upto what +1 (range ends with n-1
        if prime_or_not[p]:#if p is true then only it will work     
            for multiple in range(p*p,n+1,p):#2*2 like that upto last
                prime_or_not[multiple]=False
    return  [p for p in range(n+1)if prime_or_not[p]]
def prime_factors(n):
    primes = sieve_of_E(n)
    factors=[]
    for p in primes:
        while n%p == 0:
            factors.append(p)
            #for count we take another loop for repeatations are count increase
            n = n//p
    return factors
n = int(input("Enter a number to find all No's: "))
print(prime_factors(n))
