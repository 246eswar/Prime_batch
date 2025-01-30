n=int(input("n: "))
a,b=0,1
print(a)
if n>0:
    print(b)
for i in range(1,n):
    a,b=b,a+b
    if b<=n:
        print(b)
