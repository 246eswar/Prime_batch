#reverse of number

num=int(input("Enter a number : "))
reverse = 0 # 123 = 321
while num > 0:#123>0,#12>0,#1>0,#0.1>0
    rem = num % 10#last digit is reminder(one digit out side)#3,#2,#1
    reverse=reverse*10+ rem#0*10+3=3,#3*10+2,#32*10+1
    num = num // 10 #12,#1,#0.1
print(reverse)


