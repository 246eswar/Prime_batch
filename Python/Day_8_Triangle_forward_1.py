
'''
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
'''
'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    print('*'*i)'''
#1. * or 1 or any element
'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print('*',end=" ")
    print()'''
#2. A,BB,CCC,DDDD...
'''n=int(input("Enter the number: "))
ch=ord('A')-1
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch+i),end=" ")
    print()'''
#3. 1,22,333,444...
'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()'''
#4.a,bb,ccc,dddd,...
'''n=int(input("Enter the number: "))
ch=ord('a')
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch+i),end=" ")
    print()'''
#5. 1,12,123,1234...
'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''
#6. a,ab,abc,abcd,.....
'''n=int(input("Enter the number: "))
ch=ord('a')-1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch+j),end=" ")
    print()'''
#7. A,AB,ABC,ABCD,.....
'''n=int(input("Enter the number: "))
ch=ord('A')-1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch+j),end=" ")
    print()'''
#7. 1,23,456,.....
'''n=int(input("Enter the number: "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()'''
#8. A,BC,DEF,.....
'''n=int(input("Enter the number: "))
ch=ord('A')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()'''
#9. a,bc,def,.....
'''n=int(input("Enter the number: "))
ch=ord('a')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()'''
