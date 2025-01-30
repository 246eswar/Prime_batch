n=int(input("Enter the valur: "))
for i in range(n):#outer loop
    for j in range(n-1-i):#spaces
        print(' ',end=" ")
    for k in range(2*i+1):#for *
        print(chr(65+i),end=" ")
    print()
(1,i+1)
(i-1,0,-1)
