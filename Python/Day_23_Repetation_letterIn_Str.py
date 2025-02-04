s=input()
count=[]
for char in s:
	if char in count:
	    print(char)
	    break
	count.append(char)
else:
    print(0)
	
