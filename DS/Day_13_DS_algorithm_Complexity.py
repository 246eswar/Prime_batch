#TIME and Space complexity
#user call then directly donot call we give extra input to choose

for i in range(1,n+1):
    sum=sum+i
    return sum

#1(i)+[n+1](for range block)+[2n times](n+n(for +)+1(assigning))+[n times](for return)
#total 4n+2
#inner loops n square times
#loop then another outside loop n+n times

#Big-Theta(O)--average--"the same as"
#Big-Oh(O)--wrost case--"more than or same as"
#Big_Omega--best case
