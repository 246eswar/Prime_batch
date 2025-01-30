#String Formats

#Modulus --->%

#old style
name="Eswar"
age=25
format_string="My name is %s and i am %d years old." %(name,age)
print(format_string)

#New style
#Dot format
format_string1="My name is {} and i am {} years old." .format(name,age)
print(format_string1)

#F_string
format_string2=f"my name is {name} and i am {age} years old."
print(format_string2)

#Named arguments
format_string3=f"{name*age}"
print(format_string3)

