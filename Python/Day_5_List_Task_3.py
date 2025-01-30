#if number is prime number then fizz, number is palindrome then buzz
#sieve of eratosthenes-->use for prime numbers
number=int(input("enter the number: "))
# Check if the number is prime
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# Check if the number is a palindrome
is_palindrome = str(number) == str(number)[::-1]

# Print "Fizz" if prime, "Buzz" if palindrome
if is_prime and is_palindrome:
    print("Fizz Buzz")
elif is_prime:
    print("Fizz")
elif is_palindrome:
    print("Buzz")

else:
    print("Neither Prime Nor Palindrome")
