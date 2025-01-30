with open("Day_14_fileHandling_1.py",'r') as file:
    print(file.read())
    file.seek(0)#it resets the cursor
    print(file.readline())
    print(file.readlines())
    
