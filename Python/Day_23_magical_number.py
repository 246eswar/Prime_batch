n = int(input())  # Read the number

# Convert the number to a string to loop through each digit
n_str = str(n)
count = 0

# Loop through each character in the string
for digit in n_str:
    if digit != '0':  # Ignore zeros
        if n % int(digit) == 0:  # Check if the digit divides n evenly
            count += 1

print(count)
