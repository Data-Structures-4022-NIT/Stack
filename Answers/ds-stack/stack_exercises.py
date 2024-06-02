class Stack:
    def __init__(self):
        self.st=[]

    #Adds an item to the top of the stack.
    def push(self, data):
        self.st.append(data)

    #Removes the item at the top of the stack and returns it.
    def pop(self):
       if len(self.st) > 0:
            remove = self.st.pop()
            return remove
       else:
        return None


    #Returns the top item of the stack without removing it.
    def peek(self):
        if len(self.st)>0:
            return self.st[len(self.st)-1]
        else:
            return None


    #Returns True if the stack is empty, otherwise False.
    def isEmpty(self):
        if len(self.st) == 0:
            return True
        else:
            return False

    #Returns the number of elements in the stack.
    def size(self):
        return len(self.st)

    #Retrieve the maximum element in the stack.
    def get_max(self):
        if not self.isEmpty():
            return max(self.st)
        else:
            return None

stack = Stack()
stack.push(100)
stack.push(10)
stack.push(20)
print(stack.get_max())    # output: 100
print(stack.peek()) # Output: 20
print(stack.pop()) # Output: 20
print(stack.isEmpty()) # Output: False

#String Reversal
def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for char in string:
        stack.push(char)
    while not stack.isEmpty():
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string("hello")) # Output: "olleh"

def evaluate_postfix(expression):
    stack = []
    operators = ['-', '*', '/', '+']
    for token in expression.split():
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token =='+':
                result = operand1 + operand2
            stack.append(result)
        else:
            stack.append(float(token))

    return stack.pop()

print(evaluate_postfix("3 4 + 2 * 7 /")) # Output: 2.0

def is_balanced(expression):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top_bracket = stack.pop()
            if bracket_pairs[top_bracket] != char:
                return False

    return len(stack) == 0

# Example usage
print(is_balanced("{[()]}")) # Output: True
print(is_balanced("({[)")) # Output: False

def prefix_to_postfix(expression):
    stack = []
    tokens = expression.split()  #Split the expression into tokens

    for i in range(len(tokens) - 1, -1, -1):  #Iterate in reverse order
        token = tokens[i]
        if token.isdigit():  #push operand  into the stack
            stack.append(token)
        else:  #If it's an operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand1 + operand2 + token)  #Append in postfix order

    return stack[0]  #Return the postfix

print(prefix_to_postfix("* + 3 4 2"))  # Output: "3 4 + 2 *"


def infix_to_postfix(infix_expr):
    stack = Stack()
    postfix_expr = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in infix_expr.split():
        if token.isdigit():
            postfix_expr.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                postfix_expr.append(stack.pop())
            if not stack.isEmpty() and stack.peek() == '(':
                stack.pop()
        else:
            while not stack.isEmpty() and precedence.get(stack.peek(), 0) >= precedence[token]:
                postfix_expr.append(stack.pop())
            stack.push(token)

    while not stack.isEmpty():
        postfix_expr.append(stack.pop())

    return ' '.join(postfix_expr)


print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"))  # Output: "3 4 2 * 1 5 - / +"

def daily_temperatures(temperatures):
    stack = []
    day = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prevday = stack.pop()
            day[prevday] = i - prevday
        stack.append(i)

    return day

print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]

def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length

print(longest_valid_parentheses("(()"))  # Output: 2
print(longest_valid_parentheses(")()())"))  # Output: 4



def sort_stack(stack):
    temp_stack = Stack()
    while not stack.isEmpty():
        item = stack.pop()
        while not temp_stack.isEmpty() and temp_stack.peek() < item:
            stack.push(temp_stack.pop())
        temp_stack.push(item)
    return temp_stack

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
sorted_stack = sort_stack(stack)
print(sorted_stack.pop())  # Output: 1
print(sorted_stack.pop())  # Output: 3
print(sorted_stack.pop())  # Output: 4
