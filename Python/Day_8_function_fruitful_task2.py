'''def sum1(a):
    if a <0:
        return "number is negative Try again"
    else:
        if a%2==0:
            return "even"
        else:
            return "odd"
b=sum1(-1)
print(b)'''

def sum1(a):
    if a >0:
        if a%2==0:
            return "even"
        else:
            return "odd"
    return "number is negative Try again"
b=sum1(-9)
print(b)
