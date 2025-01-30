#start:end:step
'''PPP
NNN
PNP
NPN
PNN
NPP'''
'''a=[10,20,30,60,70,40,50]
print(a[0:3])
print(a[0:7:2])
print(a[-3:])
print(a[1:-1:2])
print(a[-1:0:-2])
print(a[0:-2])
print(a[-1:2:-1])'''

#take a integer numbers list from user and sum the list
a=list(map(int,input("enter the list: ").split()))
#at a time two things are done use map(--,--)
print(a)
sum1=0
for i in a:
    sum1+=i
print(sum1)
max1=a[0]
for j in a:
    if(j>max1):
        max1=j
print(max1)
