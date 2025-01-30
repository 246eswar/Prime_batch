#remove duplicates from a list while maintaining the order of elements
'''a=[10,20,30,40,50,20,40]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''

#check if a list is sorted in ascending order
'''a=[10,49,38,46,86]
a.sort()
print(a)'''

#merge two lists into one
'''a=[10,29,37,48]
b=[35,46,58,99]
c=a+b#for merge use +
print(c)
a.extend(b)#extend
print(a)'''
#another method
a=[10,29,37,48]
c=[35,46,58,99]
b=[]
for i in a:
    b.append(i)
for i in c:
    b.append(i)
print(b)
