# Input string
string = input("Enter a string with parentheses: ")

# Initialize variables to track depth and errors
depth = 0
max_depth = 0
errors = 0

# Iterate over each character in the string
for char in string:
    if char == '(':  # Opening parenthesis increases depth
        depth += 1
        max_depth = max(max_depth, depth)
    elif char == ')':  # Closing parenthesis decreases depth
        depth -= 1
        if depth < 0:  # If depth is negative, we have an unmatched closing parenthesis
            errors += 1
            break

# Final check for unmatched opening parentheses
if depth > 0:
    errors += depth  # Count the unmatched opening parentheses as errors

# Output result based on errors
if errors == 0:
    print(f"valid and depth: {max_depth}")
else:
    print(f"not valid and errors: {errors}")
