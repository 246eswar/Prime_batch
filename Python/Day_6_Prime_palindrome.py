#prime and pallindrome --> madam explaining
#range
start=1
end=100
for number in range(start,end+1):
    is_prime=True
    if number <= 1:
        is_prime=False
    else:
        for i in range(2,int(number**0.5)+1):#iterrate number
           if number % i ==0:
                is_prime=False
                break
    str_num=str(number)
    is_palindrome=str_num==str_num[::-1]
    if is_prime and is_palindrome:
        print("FizzBuzz")
    elif is_prime:
        print("Fizz")
    elif is_palindrome:
        print("Buzz")
    else:
        print(number)#,"is neither palindrome nor prime number")

    
        
        
