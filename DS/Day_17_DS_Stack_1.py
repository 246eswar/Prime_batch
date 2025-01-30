#STACK
#1.take empty list
stack=[]
stack.append(10)#PUSH Operation
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
top_element=stack[-1]#peek or top operation
print(top_element)
stack.pop()#pop operation
print(stack)
size=len(stack)
print(size)#size
is_empty=len(stack)==0
print(is_empty)
