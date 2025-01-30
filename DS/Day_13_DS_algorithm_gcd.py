def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(48,18))

'''
FUNCTION gcd(a,b)
    WHILE b!=0 THEN
        temp = b
        b = a MOD b
        a = temp        
        #a,b=b,a MOD b(it is not understand)
    END WHILE
    RETURN a
END FUNCTION
'''
