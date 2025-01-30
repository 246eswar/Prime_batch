#default
a={1:"one",2:"two",3:"three"}
b={1,2,3,4,5,6}
c="team"
dict1=dict.fromkeys(a,b)
dict2=dict.fromkeys(b,c)
print(dict1)
print(dict2)
d={'main','ad','th'}
dict3=dict.fromkeys(b,d)
print(dict3)
dict3.setdefault(6,'ufuf')
print(dict3)
#if value already present not add
dict3.setdefault(7,'due to')
print(dict3)
# need both of keys and values
print(dict3.items())
dict2.clear()
print(dict2)


