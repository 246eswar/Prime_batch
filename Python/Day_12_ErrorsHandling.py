#try method -->first block
#finally block -->it executes confirmly even if error cames
#expect  -->last block
#try block line by line checking
def num(n1,n2):
    try:
        res=n1/n2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError as e:
        print("Invalid input type")
    else:
        print("Division Successfully")
        print(res)
    finally:
        print("Execution completed")

num(3,0)
print()
num(10,3)
print()
num(10,'z')
    
    
