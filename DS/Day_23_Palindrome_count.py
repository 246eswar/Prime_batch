a=input().split()
count=0
for i in a:
	if i==i[::-1]:
		count+=1
print(count)
