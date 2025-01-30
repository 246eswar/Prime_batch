#Palindrome
num=int(input("Enter a number : "))
reverse = 0 
temp = num
while num > 0:
    rem = num % 10
    reverse=reverse*10+ rem
    num = num // 10 
print(reverse)

if temp == reverse:
    print("palindrome number ")
else:
    print("not a palindrome number ")
