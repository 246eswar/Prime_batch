#for list comprehesation
'''sq=[x**2 for x in range(21)]
print(sq)'''

#for dictionary comprehesation
'''sq1={x:x**2 for x in range(21)}
print(sq1)'''

#for even
'''sq2_even={x:x**2 for x in range(21) if x%2 == 0}
print(sq2_even)'''

'''{expression  loop (condition is optional)}'''
'''sqq={x:x%2 for x in range(10)}
print(sqq)'''
#self relation and factorial are do in comprehension

names=['vick','ram',' ']
a={name:len(names) for name in names }
print(a)
