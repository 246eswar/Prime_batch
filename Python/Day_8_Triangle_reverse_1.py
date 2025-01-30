'''
1 1 1 1 1
1 1 1 1
1 1 1
1 1
1'''
##1. * or 1 or any element
'''n=int(input("Enter the valur: "))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end="")
    print()'''
#2. ....DDDD,CCC,BB,A
'''n=int(input("Enter the number: "))
ch=ord('A')-1
for i in range(n,0,-1):
    for j in range(i):
        print(chr(ch+i),end=" ")
    print()'''
#3. ...4444,333,22,1
'''n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()'''
#4....dddd,ccc,bb,...
'''n=int(input("Enter the number: "))
ch=ord('a')
for i in range(n,0,-1):
    for j in range(i):
        print(chr(ch+i),end=" ")
    print()'''
#5. ....1234,123,12,1
'''n=int(input("Enter the number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
#6. ...abcd,abc,ab,a
'''n=int(input("Enter the number: "))
ch=ord('a')-1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(ch+j),end=" ")
    print()'''
#7. ...ABCD,ABC,AB,A
'''n=int(input("Enter the number: "))
ch=ord('A')-1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(ch+j),end=" ")
    print()'''
#8. 1,23,456,.....
'''n=int(input("Enter the number: "))
num=n*(n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()'''
#9. A,BC,DEF,.....
#error
n=int(input("Enter the number: "))
ch=chr('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch+n-1),end=" ")
        ch-=1
    print()
#10. a,bc,def,.....
#error
'''n=int(input("Enter the number: "))
ch=ord('a')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()'''

