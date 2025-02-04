def sieve_of_E(n):
    #fixed size
    prime_or_not = [True]*(n+1)#initially all are taken True
    prime_or_not[0] = prime_or_not[1] = False #0&1 are not prime numbers
    for p in range(2,int(n**0.5)+1):
    #starting point is 2 and ending point upto what +1 (range ends with n-1
        if prime_or_not[p]:#if p is true then only it will work     
            for multiple in range(p*p,n+1,p):#2*2 like that upto last
                prime_or_not[multiple]=False
    primes = [p for p in range(n+1)if prime_or_not[p]]
    return primes
n = int(input("Enter a number to find all No's: "))
print(sieve_of_E(n))        
