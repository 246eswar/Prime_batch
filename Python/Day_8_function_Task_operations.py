'''take a function the input should be given by the user
if input is +,-,*,/,& operation any two (+- then division)'''


def fun(n1,n2,s1,s2,a):
    if a=='&' or a=='^' or a=='|':
        s1=set(map(int,input("s1: ").split()))
        s2=set(map(int,input("s2: ").split()))
        if a == '^':
            return s1^s2
        elif a == '|':
            return s1|s2
        elif a == '&':
            return s1&s2
    elif a=='+' or a=='-' or a=='+-':
        n1=int(input("n1: "))
        n2=int(input("n2: "))
        if a == '+':      
            return n1+n2
        elif a == '-':   
            return n1-n2   
        elif a == '+-':   
            return n1/n2
    else:
        return "please give correct operator"
a=input("Enter any of one of -->  +  - | & ^: ")
print(fun(n1,n2,s1,s2,a))
