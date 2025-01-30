#Autobiological Number
'''an autobiographical Number is a number
N such that the first digit of N represents
the count of how many zeros are there in N,
the second digit represents the count of
how many ones are there in N and so on
you are given a function,
findAutoCount(n):
The function accepts string "n" which is a
number and checks whether the number is
autobiogrphical number or not.If it is,
an interger is returned, i.e., the count
of distinct numbers in 'n'. If not, it return 0.
Assumption:
The input string will not be longer than 10
characters
Input string will consist of numeric characters.
Note:
If string is None Return 0
'''
#explanation
'''0th position in the input contains the number
of 0 present in input, i.e.,1, in 1st position
the count of number of 1s in input i.e., 2, in
2nd position the count of 2s in input i.e. 1,
and in 3rd position the count of 3s i.e. 0,so the
number is an'''

def autocount(num):
    if num is None:
        return 0
    if not num.isdigit():
        return 0
    l = len(num)
    count=[0]*10#repeatation
    for digit in num:
        count[int(digit)]+=1
    for i in range(l):
        #tally the count digits (compare)
        if int(num[i]) != count[i]:
            return 0
        return len(set(num))#no repeatetions in set
        #index value and count of that index value element is equal
input1="1111210"
input2="2020"
input3="3211000"
print(autocount(input1))
print(autocount(input2))
print(autocount(input3))
                
    
        



    
