#even or ODD using While Loop
'''
num=int(input("Enter a number : "))
i = 1
while i <= num:
    if i %2 == 0:
        print(i,"even number")
    else:
        print(i,"odd number")
    i += 1'''
'''
#print sum of even and odd
num=int(input("Enter a number : "))
i = 1
sum_of_even=0
sum_of_odd=0
while i <= num:
    if i %2 == 0:
        print(i,"even number")
        sum_of_even += i
    else:
        print(i,"odd number")
        sum_of_odd += i
    i += 1
print("sum of given even numbers = ", sum_of_even)
print("sum of given odd numbers = ", sum_of_odd)
'''
