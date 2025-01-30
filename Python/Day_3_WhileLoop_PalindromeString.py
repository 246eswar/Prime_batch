string = input("Enter a string : ")
reverse = ''#empty string
i=len(string)-1#reads upto zero
while i >= 0:
    reverse= reverse + string[i]
    i -= 1
print(reverse)
if(string == reverse):
    print("palindrome")
else:
    print("not a palindrome")
