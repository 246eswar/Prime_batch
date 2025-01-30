#4 types arguments
'''1. required arguments--> parameters are same in top and bottom'''
'''def fun(name):
    print("every "+ name)
name="hi"
fun(name)'''
#2.keyword arguments
'''def fun(name1,name2):
    print("every "+ name1 + name2)
fun("qis","iit")#order follows'''
"""def fun(name1,name2):
    print("every "+ name1 + name2)
fun(name2="qis",name1="iit")#argument"""
#for diifferent data types
'''def fun(name1,name2):
    print("every ", name1 , name2)
fun(name2="qis",name1=4)'''
#3. Default arguments
'''def fun(name1,name2=6):#name2=6 is default
    print("every ", name1 , name2)
fun("qis")'''
'''def fun(name1,name2=6):#name2=6 is default
    print("every ", name1 , name2)
fun("qis","iit")#input is given so default is neglect'''
#input is first priority --> highest priority than default

#4.variable length arguments
def fun(*arg):# * for repeation only tuple its takes because it is immutable
    print("every ",arg)
fun(10)
fun(10,20,30,40)
fun(10,'op',20)
