'''
150. Evaluate Reverse Polish Notation (Medium)
Problem Statement

You are given an array of strings tokens representing an arithmetic
expression in Reverse Polish Notation (postfix).

Evaluate the expression and return the integer result.

Valid operators are +, -, *, /. Each operand is an integer.
Division between two integers always truncates toward zero.

Example
Input:
tokens = ["2","1","+","3","*"]

Output:
9

Explanation:
((2 + 1) * 3) = 9
'''

def evalRPN(tokens):
    stack = []                       # operand stack

    for tok in tokens:
        if tok in ("+", "-", "*", "/"):
            b = stack.pop()          # second operand (top)
            a = stack.pop()          # first operand
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                # int(a / b) truncates toward zero (unlike floor //)
                stack.append(int(a / b))
        else:
            stack.append(int(tok))   # operand

    return stack[0]


if __name__ == "__main__":
    print(evalRPN(["2", "1", "+", "3", "*"]))  # Expected: 9
    print(evalRPN(["4", "13", "5", "/", "+"]))  # Expected: 6
    print(evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    ))  # Expected: 22


'''
Pattern
✅ Stack (operand stack for postfix evaluation)
In postfix, each operator acts on the two most recent operands, so a LIFO
stack naturally holds pending operands until an operator consumes them.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Each token is processed once and must be read at least once; O(n) is optimal.
'''
