#Finding Minimum Number of Houses to Feed all Rats:
'''The function  accepts two positive integers 'r' and 'unit'
and a positive integer array 'arr' of size 'n' its argument 'r'
represents the number of rats present in area,'unit' is the amount
of food each rat consumes and ith element of array'arr' represent
the amount of food present in "i+1" house number, where 0 <= i
Note:
Return -1 if the array is null
Return 0 if the total amount of food from all houses
is not sufficient for all the rats'''

'''r=int(input("Number of Rats: "))
unit=int(input("weight of each Rat consume: "))
arr=int(input("number of Houses: "))
required= r * unit
li=[]
count=0
for i '''

'''
r=7
unit=5
arr=8
list1=[2,5,8,6,9,7,7,8]
re=r*unit
c=0
if len(list1) == 0:
    print("-1")
for i in range(len(list1)):
    if c < re:
        c=c+list1[i]
    else:
       print(i)
       break
print(0)'''

#madam explain
def find_houses(r,units,arr):
    if len(arr)==0:
        return -1
    food = r * units
    f=0
    for i,fd in enumerate(arr):
        f=f+fd#fd is iterrate
        if f >= food:
            return i + 1#houses starts with 1st
    return 0
r=6
units=4
arr=[8,2,5,7,8,3,7]
'''
r=int(input("Rats: "))
units=int(input("units: "))
arr=list(map(int,input("list: ).split()))
'''
print(find_houses(r,units,arr))
        



