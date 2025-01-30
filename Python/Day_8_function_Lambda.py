#python anonymous/Lambda function
#without using function name call function by using lambda
'''lambda arguments:expression'''
'''#basic dynamic function
def add(x,y):
    return x+y
a=add(16,8)
print(a)'''

'''a=lambda x:x*2
print(a(5))

a=lambda x,y:x*y
print(a(5,5))
'''
'''a=lambda x,y:x*y
b=lambda x,y:x/y
c=lambda x,y:x%y
print(a(5,5))
print(b(6,5))
print(c(7,8))'''

#condition is related to any one of the argument
#expression only one
'''a=lambda x,y,z:x*y-z if y!=0 else 'eeror'
print(a(4,6,9))'''
'''b=lambda x,y:x/y if y!=0 else 'cannot divide'
print(b(6,4))
print(b(4,0))'''




