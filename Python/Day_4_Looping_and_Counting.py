#count is counts the similar types
'''a="Welcome to QIS college"
count=0#initial count is Zero
for i in a:
    if i == 'e':
         count += 1
print(count)
'''

#COUNT Method
'''a="Welcome to QIS tocollege"
print(a.count('e'))     '''   

a="t o Welcome t oo QIS to college"
print(a.count('to'))    
#if not available then zero
#it is not cutomize error
#it counts the spaces
print(a.count('t o'))
print(a.count('t o '))
print(a.count('t o  '))
