#Electricity Calculation

#Take the input(units)
'''0-50--80
51-100---1.69
101-150---2.89
150-200--4.56
200-300-5.34
300-400-5.99
400-500-6.89
500-750-7.56
750-----8.73'''

u=int(input("Enter number of units : "))
if(u<=50):
    bill=80
elif (u>50 and u<=100):
    bill= 80 + (u-50)*1.69
elif (u>100 and u<=150):
    bill=80+((100-50)*1.69)+((u-100)*2.89)
elif (u>150 and u<=200):
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((u-150)*4.56)
elif (u>200 and u<=300):
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((200-150)*4.56)+((u-200)*5.34)
elif (u>300 and u<=400):
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((200-150)*4.56)+((300-200)*5.34)+((u-300)*5.99)
elif (u>400 and u<=500):
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((200-150)*4.56)+((300-200)*5.34)+((400-300)*5.99)+((u-400)*6.89)
elif (u>500 and u<=750):
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((200-150)*4.56)+((300-200)*5.34)+((400-300)*5.99)+((500-400)*6.89)+((u-500)*7.56)
elif u>750:
    bill=80+((100-50)*1.69)+((150-100)*2.89)+((200-150)*4.56)+((300-200)*5.34)+((400-300)*5.99)+((500-400)*6.89)+((750-500)*7.56)+((u-750)*8.73)
print(bill)


