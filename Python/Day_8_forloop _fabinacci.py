n=int(input("Enter the number: "))
a,b=0,1
print(a)
print(b)
for i in range(1,n+1):
    a,b=b,a+b
if b<=n:
    print(b)
else:
    break
