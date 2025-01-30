#slicing--> to access the sub strings
'''[:] indicate starting and ene point
[0:]-->zero is starting
[:]     -->is also start with zero
[3:] -->is start with 3
[:] -->is also ends with last position
[:5]-->start at zero position and end 5th position'''

'''a="mam told \"come fast\""
print(len(a))
print(a[:])
print(a[:20])
print(a[0:19])'''

#slicing_steps
'''a="mam told \"come fast\""
print(len(a))
print(a[:])
print(a[:20:2])
print(a[-10:-1])#starting value start with less i.e.-10<-1
print(a[-10:-1:2])

print(a[-1:-10])#no error comes and print only Blank
#Interpreter is struck and not understand so it print EMPTY
print(a[-1:-10:-1])#-1 works as direction reverse order'''

#start point as positive and end point i negative
a="mam told \"come fast\""
#print(a[1:-7])
#print(a[15:-17])#criscross then empty space will come
#print(a[15:-17:-1])#output is come
#print(a[-1:10])#empty criss cross
#print(a[-17:15:-1])#criss cross
print(a[-17:15:1])
