#operation is enough then we use void
#void which does not return any value
#return statement is not there then the function is void
#codition --return in if condition if condition fails in else no return
def sum1(a):
    if a <0:
        return "number is negative Try again"
    else:
        print(a)
    print(a*2)           
#fruitful declare means that function has return
#not in one condition
#function based

'''based on data'''
def sum1(a):
    if a <0:
        return "number is negative Try again"
    else:
        print(a)
        return -1
    print(a*2)
    
'''fruitful'''
def sum1(a):
    if a <0:
        return "number is negative Try again"
    else:
        print(a)
        return -1
    return a*2



