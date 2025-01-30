#delete element
'''1.remove(on the bases of DATA)'''
'''a=[1,2,3,6,'po','ra',['ram','syam'],'wa',4,5]
a.remove('po')
#remove with the data
print(a)
#a.remove(7)
#index value don't work
print(a)
a.remove(['ram','syam'])
print(a)
#sublist also removed'''

#pop -->will delete the last data
'''a=[1,2,3.9,6,'po','ra',['ram','syam'],'wa',4,5]
a.pop()#default last index position
print(a)
a.pop(3)
print(a)#perticular index data it will delete
#a.pop(a[2])#float cannot be interpreter as a integer
#so don't give a[4] and give direct index value
print(a)
#pop is navigate through index values
#Direct way()
#indirect way a[]'''

#3.delete -->entire list delete
#delete is not a method it is a fuction it delete entaire thing
a=[1,2,3.9,6,'po','ra',['ram','syam'],'wa',4,5]
a.pop()
del a[2]
#del a['po']
print(a)

#remove --> data
#pop and del are index
