o=input("operators(+,-,^,|,+-): ")
def cal():
    if o=='^' or o=='|' or o=='&':
        l1=list(map(int,input("set1: ").split()))
        l2=list(map(int,input("set1: ").split()))
        s1=set(l1)
        s2=set(l2)
        if o=='^':
            return s1^s2
        if o=='|':
            return s1|s2
        if o=='&':
            return s1&s2
    elif o=='+' or o=='-' or o=='+-':
        v1=int(input("n1: "))
        v2=int(input("n2: "))
        if o=='+':
            return v1+v2
        if o=='-':
            return v1-v2
        if o=='+-':
            return v1/v2
    return "please give correct operator"
print(cal())
