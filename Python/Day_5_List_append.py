#append is add is what is we given
'''list1=[1,2,3,4,5]
list1.append(34)
print(list1)
list2=['ras','edr','rffrr']
list2.append('fgdf')
print(list2)'''

#insert , extend
'''list1=[1,2,3,4,5]
list1.append(34)
list1.insert(4,'college')#index value based
print(list1)
list1.extend('college')#individual letters add
#extend is divide based on index
print(list1)
a=5
list1=list1,a
print(list1)'''

a=[1,2,3,4,5]
b=['college','rama','siva']
a.append(b)
print(a)
a.insert(4,b)
print(a)
a.extend(b)
print(a)    
c=[1,2]
a[4][0]=['r','t','u']#modify
print(a)
#count variable
print(a.count('t'))#substrings are not counted
print(a.count("['r','t','u']"))
print(a.count([['r', 't', 'u'], 'rama', 'siva']))
print(a.count([1, 2, 3, 4, [['r', 't', 'u'], 'rama', 'siva'], 5, [['r', 't', 'u'], 'rama', 'siva'], 'college', 'rama', 'siva']))
#total list is given then zero
#sublist is given then count is happen
#sub-sublist is given then won't count
