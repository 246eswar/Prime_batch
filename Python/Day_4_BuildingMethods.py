#searching is done in comparision operation ,condion and itteration
#use find (it search it is available or not)(.(DOT)Operator we use)
'''a="mam told \"come fast\""
print(a.find('t'))'''
#find will take first occurance only
'''print()
a="mam told \"t come fast\""
print(a.find('t',5))'''
#skip the first 4 letters and start search after that
'''print()
a="mam told \"t come t  tfast\""
print(a.rfind('t'))'''
#rfind-->Reverse find last index value
'''a="mam told \"t come t  tfast\""
print(a.find('z'))'''
#visulise not eeror not shown-->error is customise{CUSTOMISE ERROR}
#error is not in red color it shown in -1
#it is replace by index

#index-->it shown error
'''a="mam told \"t come t  tfast\""
print(a.index('t'))'''

'''a="mam told \"t come t  tfast\""
print(a.rindex('z'))'''

#MIX starting and ending point-->middle part range
#position starting and ending with perticular
a="mam told \"t come t  tfast\""
print(a.index('t',5,11))
