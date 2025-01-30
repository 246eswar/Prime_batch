#set add of set
'''set1={}
print(type(set1))
a={1}
print(type(a))
a.add(2)
print(a)
a.add('op')
print(a)
a.add(7)
print(a)'''

#update set
'''a={1,2,3,4}
b={5,6,7,8}
a.update(b)
print(a)'''

#remove(raise error if not there) ,
#discard(it won't raise error)
a={1,2,3,4}
b={5,6,7,8}
a.update(b)
print(a)
a.remove(2)
print(a)
'''a.remove(2)#error raise
print(a)'''
a.discard(2)
print(a)
c={'op','bp','cp'}
a.update(c)
#multiple values then give in list or tuple
a.update([10,18])
print(a)
a.remove('op')
print(a)
a.discard('op')
print(a)

#set is mutable
#elements of set is immutable
'''d={8,9,11,15,[24,50]}#not print list is mutable
print(d)
e={8,9,11,15,(24,50)}#tuple is immutable no error
print(e)

