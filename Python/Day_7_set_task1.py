#take 3 sets and do union of two and output is do inserction with third one
a={1,2,3,4,5}
even={2,4,6,8}
odd={1,3,5,7,9}

b=(a | even)
print(b)

c=(b&odd)
print(c)
