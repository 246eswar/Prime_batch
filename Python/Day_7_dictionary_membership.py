#in operator
a={1:"one",2:"two",3:"three"}
print(1 in a)

print("two" in a)
#values are given then it takes as it is a key
b=a.copy()
print(b)

#update
c={4:"four",5:"five",6:"six"}
a.update(c)
print(a)


