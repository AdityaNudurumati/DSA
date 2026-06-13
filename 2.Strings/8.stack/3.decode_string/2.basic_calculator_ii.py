'''
2. Basic Calculator II (Medium)
Problem Statement

Given a string s which represents an arithmetic expression, evaluate it and return
its value. The expression contains non-negative integers and the operators
+, -, *, / (no parentheses). Integer division truncates toward zero.

You may assume the expression is always valid.

Example
Input:
s = "3+2*2"

Output:
7
'''

def calculate(s):

    stack = []
    num = 0
    op = '+'             # operator that precedes the current number; start with '+'

    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)          # build multi-digit number

        # act on a number when we hit an operator or the end of the string
        if (not c.isdigit() and c != ' ') or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)     # higher precedence: fold now
            else:  # '/'
                # truncate toward zero (int() not floor) for negatives
                stack.append(int(stack.pop() / num))
            op = c       # remember this operator for the next number
            num = 0

    return sum(stack)    # remaining + / - terms just add up


if __name__ == "__main__":
    print(calculate("3+2*2"))     # Expected: 7
    print(calculate(" 3/2 "))     # Expected: 1
    print(calculate(" 3+5 / 2 ")) # Expected: 5

'''
Pattern
✅ Stack (defer +/-, fold * and / immediately)
Push +num / -num; for * and / pop the top and combine right away so precedence is
handled without parsing. The final answer is the sum of the stack.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
✅ Space can drop to O(1) by tracking only the last term instead of a full stack,
but the stack version is the clearest to reason about.
'''
