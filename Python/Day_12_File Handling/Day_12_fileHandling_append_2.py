with open("Day_14_fileHandling_write_1.py",'a') as file:#w --> write    
    file.write("This is a new line \n")
with open("Day_14_fileHandling_write_1.py",'r') as file:    
    print(file.read())
