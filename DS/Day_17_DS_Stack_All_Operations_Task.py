#take a list append in stack list's last element in stacks first element
#lists first element is in stacks top element
def push():
    n=int(input("enter: "))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,"is inserted into stack")
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"is deleted from stack")
        del stack[0]          
def peek():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"is the top most element in stack")
def size():
    if len(stack)==0:
        print("stack is empty")
    else:
        size=len(stack)
        print("The size of stack is",size)
def is_empty():
    if len(stack)==0:
        print("stack is empty")
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("Elements of stack are:")
        for i in stack:
            print(i)
stack=list()            
while(1):
    print("Enter the operation")
    print("1-->push operation")
    print("2-->pop operation")
    print("3-->peek operation")
    print("4-->size operation")
    print("5-->is_empty")
    print("6-->display")
    option=input()
    if option=='1':        
        print("push operation")
        push()
    elif option=='2':        
        print("pop operation")
        pop()
    elif option=='3':        
        print("peek operation")
        peek()
    elif option=='4':        
        print("size operation")
        size()
    elif option=='5':        
        print("is_empty")
        is_empty()
    elif option=='6':
        print("display")
        display()
    else:
        print("Exit the program")
        break
    
