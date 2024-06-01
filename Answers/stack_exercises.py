class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        max_index = 0
        for i in range(0, self.size()):
            if self.items[i] > self.items[max_index]:
                max_index = i
        return self.items[max_index]


def reverse_string(input_string):
    s = Stack()
    for char in input_string:
        s.push(char)

    reversed_string = ''
    while not s.isEmpty():
        reversed_string += s.pop()

    return reversed_string


def is_operator(char):
    return char in '*-+/^'


def evaluate_postfix(expression):
    s = Stack()
    for char in expression.split():
        if is_operator(char):
            operand2 = s.pop()
            operand1 = s.pop()
            result = None
            if char == '*':
                result = operand1 * operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '+':
                result = operand1 + operand2
            elif char == '/':
                if operand2 == 0:
                    raise ZeroDivisionError("Division by zero")
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ^ operand2
            s.push(result)
        else:
            s.push(int(char))

    return s.pop()


def is_balanced(expression):
    matching = {')': '(', '}': '{', ']': '['}
    s = Stack()
    for char in expression:
        if char in matching.values():
            s.push(char)
        elif char in matching.keys():
            if s.isEmpty() or matching[char] != s.pop():
                return False

    return s.isEmpty()


def prefix_to_postfix(expression):
    s = Stack()
    for char in expression.split()[::-1]:
        if is_operator(char):
            operand1 = s.pop()
            operand2 = s.pop()
            post_ex = operand1 + " " + operand2 + " " + char
            s.push(post_ex)
        else:
            s.push(char)

    return s.pop()


def sort_stack(stack):
    temp_s = Stack()
    while not stack.isEmpty():
        temp = stack.pop()
        while not temp_s.isEmpty() and temp < temp_s.peek():
            stack.push(temp_s.pop())
        temp_s.push(temp)

    while not temp_s.isEmpty():
        stack.push(temp_s.pop())

    return stack


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(expression):
    output = []
    stack = Stack()

    char = expression.split()

    for i in char:
        if i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(i):
            while not stack.isEmpty() and (precedence(stack.peek()) >= precedence(i)):
                output.append(stack.pop())
            stack.push(i)
        else:
            output.append(i)

    while not stack.isEmpty():
        output.append(stack.pop())

    return ' '.join(output)


def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = Stack()

    for i, current_temp in enumerate(temperatures):
        while not stack.isEmpty() and temperatures[stack.peek()] < current_temp:
            index = stack.pop()
            result[index] = i - index
        stack.push(i)

    return result

def longest_valid_parentheses(str):
    stack = Stack()
    stack.push(-1)
    max_length = 0

    for i, char in enumerate(str):
        if char == '(':
            stack.push(i)
        else:
            stack.pop()
            if stack.isEmpty():
                stack.push(i)
            else:
                max_length = max(max_length, i - stack.peek())

    return max_length
