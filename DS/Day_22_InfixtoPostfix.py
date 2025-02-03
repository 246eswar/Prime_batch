class infixToPostfix:
    precedence = {'^': 5, '*': 4, '/': 4, '%': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if not self.isEmpty() else None

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if not self.isEmpty() else None

    def isOperand(self, char):
        return char.isalnum()  # Checks if the character is A-Z or 0-9

    def isValidExpression(self, expr):
        valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/%^()")
        return all(char in valid_chars for char in expr)  # Ensures only valid characters are present

    def hasBalancedParentheses(self, expr):
        stack = []
        for char in expr:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False  # More closing parentheses than opening
                stack.pop()
        return not stack  # Stack should be empty if parentheses are balanced

    def isValidOperatorPlacement(self, expr):
        prev = None
        for char in expr:
            if char in "+-*/%^" and (prev is None or prev in "+-*/%^("):  
                return False  # Detects cases like "A+*B", "+A", "(+A"
            prev = char
        return True

    def convertInfixToPostfix(self, expr):
        if not self.isValidExpression(expr):
            return "Incorrect infix expr"
        if not self.hasBalancedParentheses(expr):
            return "Incorrect infix expr"
        if not self.isValidOperatorPlacement(expr):
            return "Incorrect infix expr"

        postfix = ""
        stack = []

        for char in expr:
            if self.isOperand(char):
                postfix += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                if not stack or stack.pop() != '(':
                    return "Incorrect infix expr"
            else:
                while stack and self.precedence[stack[-1]] >= self.precedence[char] and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(char)

        while stack:
            if stack[-1] == '(':
                return "Incorrect infix expr"
            postfix += stack.pop()

        return postfix

# Taking user input
expr = input("Enter a valid infix expression where operator is placed between the operands: ")
ip = infixToPostfix()
result = ip.convertInfixToPostfix(expr)
print(result if result == "Incorrect infix expr" else f"The postfix expression of: {expr} is {result}")
