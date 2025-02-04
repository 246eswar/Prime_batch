s=input()
t=input()
c=[]
d=[]
for i in s:
	c.append(ord(i))
for j in t:
	d.append(ord(j))
a=sorted(c)
b=sorted(d)
if a==b:
	print("true")
else:
	print("false")
