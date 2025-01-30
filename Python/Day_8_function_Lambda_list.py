#lambda with list
a=[1,2,3,4,5]
b=list(map(lambda x:x*2,a))
print(b)

a=['1','2','3','4','5']
b=list(map(lambda x:x*2,a))
print(b)

a=['1','2','3','4','5']
b=list(map(lambda x:len(x),a))
print(b)

a=['1dfd','2ddfdf','f3','fff4','ffffsd5']
b=list(map(lambda x:len(x),a))
print(b)
