class FixedSizeStack:
    def __init__(self,max_size):
        self.stack=[0] * max_size
        self.top=-1
        self.max_size=max_size
    def push(self, value):
        # Check if stack is full
        if self.top < self.max_size - 1:
            self.top += 1
            self.stack[self.top] = value
        else:
            print("Stack Overflow! Cannot push more elements.")
    
    def pop(self):
        # Check if stack is empty
        if self.top >= 0:
            popped_value = self.stack[self.top]
            self.top -= 1
            return popped_value
        else:
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
    
    def peek(self):
        # Return the top element without removing it
        if self.top >= 0:
            return self.stack[self.top]
        else:
            print("Stack is empty!")
            return None
    
    def is_empty(self):
        # Check if stack is empty
        return self.top == -1
    
    def is_full(self):
        # Check if stack is full
        return self.top == self.max_size - 1
    def display(self):
        # Display the stack from bottom to top
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack contents (bottom to top):")
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
            print()  # Newline after displaying the stack

stack = FixedSizeStack(5)
stack.push(10)
stack.push(20)
stack.push(30)

print("Peek top element:", stack.peek())  
print("Pop top element:", stack.pop())   
print("Is stack empty?", stack.is_empty()) 
print("Is stack full?", stack.is_full())
stack.display() 
