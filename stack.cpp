#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <cmath>
#include <unordered_map>
#include <algorithm>
#include <sstream>

class Stack {
private:
    std::vector<int> items;

public:
    void push(int item) {
        items.push_back(item);
    }

    bool isEmpty() const {
        return items.empty();
    }

    int pop() {
        if (isEmpty()) {
            return -1; // Return -1 to indicate an empty stack
        }
        int item = items.back();
        items.pop_back();
        return item;
    }

    int peek() const {
        if (isEmpty()) {
            return -1; // Return -1 to indicate an empty stack
        }
        return items.back();
    }

    int size() const {
        return items.size();
    }

    int getMax() const {
        if (isEmpty()) {
            return -1; // Return -1 to indicate an empty stack
        }
        return *std::max_element(items.begin(), items.end());
    }
};

std::string reverseString(const std::string &inputString) {
    Stack s;
    for (char ch : inputString) {
        s.push(ch);
    }

    std::string reversedString;
    while (!s.isEmpty()) {
        reversedString += s.pop();
    }

    return reversedString;
}

bool isOperator(char ch) {
    return ch == '*' || ch == '-' || ch == '+' || ch == '/' || ch == '^';
}

int evaluatePostfix(const std::string &expression) {
    Stack s;
    std::stringstream ss(expression);
    std::string token;
    while (ss >> token) {
        if (isOperator(token[0]) && token.length() == 1) {
            int operand2 = s.pop();
            int operand1 = s.pop();
            int result = 0;
            switch (token[0]) {
                case '*':
                    result = operand1 * operand2;
                    break;
                case '-':
                    result = operand1 - operand2;
                    break;
                case '+':
                    result = operand1 + operand2;
                    break;
                case '/':
                    if (operand2 == 0) {
                        throw std::runtime_error("Division by zero");
                    }
                    result = operand1 / operand2;
                    break;
                case '^':
                    result = std::pow(operand1, operand2);
                    break;
            }
            s.push(result);
        } else {
            s.push(std::stoi(token));
        }
    }

    return s.pop();
}

bool isBalanced(const std::string &expression) {
    std::unordered_map<char, char> matching = {{')', '('}, {'}', '{'}, {']', '['}};
    Stack s;
    for (char ch : expression) {
        if (matching.count(ch) == 0) {
            s.push(ch);
        } else {
            if (s.isEmpty() || s.pop() != matching[ch]) {
                return false;
            }
        }
    }
    return s.isEmpty();
}

std::string prefixToPostfix(const std::string &expression) {
    Stack s;
    std::stringstream ss(expression);
    std::vector<std::string> tokens;
    std::string token;

    while (ss >> token) {
        tokens.push_back(token);
    }

    std::reverse(tokens.begin(), tokens.end());

    for (const std::string &token : tokens) {
        if (isOperator(token[0]) && token.length() == 1) {
            std::string operand1 = s.pop();
            std::string operand2 = s.pop();
            std::string postExp = operand1 + " " + operand2 + " " + token;
            s.push(postExp);
        } else {
            s.push(token);
        }
    }

    return s.pop();
}

Stack sortStack(Stack stack) {
    Stack tempStack;
    while (!stack.isEmpty()) {
        int temp = stack.pop();
        while (!tempStack.isEmpty() && temp < tempStack.peek()) {
            stack.push(tempStack.pop());
        }
        tempStack.push(temp);
    }
    while (!tempStack.isEmpty()) {
        stack.push(tempStack.pop());
    }
    return stack;
}

int precedence(char op) {
    if (op == '+' || op == '-') {
        return 1;
    }
    if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

std::string infixToPostfix(const std::string &expression) {
    std::vector<std::string> output;
    Stack stack;
    std::stringstream ss(expression);
    std::string token;

    while (ss >> token) {
        if (token == "(") {
            stack.push(token[0]);
        } else if (token == ")") {
            while (!stack.isEmpty() && stack.peek() != '(') {
                output.push_back(std::string(1, stack.pop()));
            }
            stack.pop();
        } else if (isOperator(token[0]) && token.length() == 1) {
            while (!stack.isEmpty() && precedence(stack.peek()) >= precedence(token[0])) {
                output.push_back(std::string(1, stack.pop()));
            }
            stack.push(token[0]);
        } else {
            output.push_back(token);
        }
    }

    while (!stack.isEmpty()) {
        output.push_back(std::string(1, stack.pop()));
    }

    std::string result;
    for (const std::string &str : output) {
        if (!result.empty()) {
            result += " ";
        }
        result += str;
    }

    return result;
}

std::vector<int> dailyTemperatures(const std::vector<int> &temperatures) {
    int n = temperatures.size();
    std::vector<int> result(n, 0);
    Stack stack;

    for (int i = 0; i < n; ++i) {
        while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
            int index = stack.pop();
            result[index] = i - index;
        }
        stack.push(i);
    }

    return result;
}

int longestValidParentheses(const std::string &str) {
    Stack stack;
    stack.push(-1);
    int maxLength = 0;

    for (int i = 0; i < str.length(); ++i) {
        char ch = str[i];
        if (ch == '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.isEmpty()) {
                stack.push(i);
            } else {
                maxLength = std::max(maxLength, i - stack.peek());
            }
        }
    }

    return maxLength;
}

int main() {
    std::string inputString = "hello";
    std::cout << "Reversed string: " << reverseString(inputString) << std::endl;

    std::string postfixExpr = "2 3 * 5 4 * + 9 -";
    std::cout << "Postfix evaluation: " << evaluatePostfix(postfixExpr) << std::endl;

    std::string balancedExpr = "{[()]}";
    std::cout << "Is balanced: " << (isBalanced(balancedExpr) ? "Yes" : "No") << std::endl;

    std::string prefixExpr = "* + 2 3 4";
    std::cout << "Prefix to Postfix: " << prefixToPostfix(prefixExpr) << std::endl;

    Stack stack;
    stack.push(3);
    stack.push(1);
    stack.push(4);
    stack.push(2);
    stack = sortStack(stack);
    std::cout << "Sorted stack: ";
    while (!stack.isEmpty()) {
        std::cout << stack.pop() << " ";
    }
    std::cout << std::endl;

    std::string infixExpr = "3 + 5 * 2 - 8 / 4";
    std::cout << "Infix to Postfix: " << infixToPostfix(infixExpr) << std::endl;

    std::vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
    std::vector<int> tempResults = dailyTemperatures(temperatures);
    std::cout << "Daily temperatures: ";
    for (int days : tempResults) {
        std::cout << days << " ";
    }
    std::cout << std::endl;

    std::string parenStr = "(()())";
    std::cout << "Longest valid parentheses: " << longestValidParentheses(parenStr) << std::endl;

    return 0;
}
