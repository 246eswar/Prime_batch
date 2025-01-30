#original content of string is not modified
#replce method is modify the string and create temporary string
#we need to store it in temporary variable
#in replacing indexing is not work
'''a="Welcome to QIS college"
print(a.replace('QIS','IIT'))#temporary change
print(a)#Original content no change'''

'''a="Welcome to QIS college"
b=a.replace('QIS','IIT')
print(a)
print(b)'''

'''a="Welcome to QIS college"
c=a.replace('o','z')#Change all "o" letters in 'a'
print(c)'''

'''a="Welcome to QIS college"
c=a.replace('o','z',2)#2 is count
print(c)'''

'''a="Welcome to QIS college"
print(a)
b=a.replace('Welcome','thank')
print(b)
c=b.replace('to','you')
print(c)
d=c.replace('QIS','visit')
print(d)
e=d.replace('college','again')
print(e)
print()
print(e)'''

a="Welcome to QIS college"
print(a)
b=a.replace('Welcome','thank')
print(b)
c=b.replace('to','you')
print(c)
d=c.replace('QIS','visit')
print(d)
e=d.replace('college','again')
print(e)
f=e.replace('hi','hello')
#it won't replace and also not given error also
#if element is present then replace otherwise it won't change anything
print(f)

