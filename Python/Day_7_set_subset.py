#set and Sub_sets
a={1,2,3,4,5,6,7,8,9}
even={2,4,6,8}
odd={1,3,5,7,9}
#here even is sub_set of a
print(even.issubset(a))
#here odd is sub_set of a
print(odd.issubset(a))
#every set is a subset of it self
print(a.issubset(a))
