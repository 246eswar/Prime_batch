#swap Upper to lower and lower to upper
#Title every first string first letter is capital
#capital only first letter of the string is capital
#entair all changes to lower or upper(.upper or .lower)
'''a="Exam ple 123 @"
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.capitalize())'''

#type checking
'''isalnum()
isalpha()
isdigit()
islower()
isupper()
isspace()
istitle()'''
'''a="Exam ple 123 @"
print(a.isupper())
print(a.islower())
print(a.isalnum())
print(a.istitle())
print(a.isdigit())
print(a.isalpha())
print(a.isspace())'''

'''a="Exam"
print(a.isupper())
print(a.islower())
print(a.isalnum())
print(a.istitle())
print(a.isdigit())
print(a.isalpha())
print(a.isspace())'''
#(Password==Password.isupper())and(Password==Password.islower())and(Password==Password.isdigit())
#task Password check
'''atleast 8 characteristics
create a loop check each character then check condition
condition minimum8,1upper,1lower,1number(digit)'''
"""Password=input("enter new password : ")
if len(Password)>=8:
    for char in Password:
        if char.isupper():
            Upper=True
        elif char.islower():
            Lower=True
        elif char.isdigit():
            Digit=True
    if Upper and Lower and Digit:
             print("Password generated successfully")
    else:
        print("weak Password")
else:
    print("Password must contain minimum 8 letters")"""

 
