'''The greatest common divisor (GCD)
of two numbers is the largest positive
integer that divides both numbers without leaving a remainder.'''

#GCD of two numbers
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))

while b != 0:
    a,b=b,a%b #a=b,b==a%b
    
print("Gcd is : ",a)

#2nd method
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
while b != 0:
    temp=b
    b=a%b
    a=temp     
print("Gcd is : ",a)

#a=12,b=14
#in while temp=14,b=2 and a=b so gcd is 2

#if zerogiven
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
if a==0 or b==0:
    print("value must not be zero")
else:
    while b != 0:
        a,b=b,a%b #a=b,b==a%b
    
    print("Gcd is : ",a)
