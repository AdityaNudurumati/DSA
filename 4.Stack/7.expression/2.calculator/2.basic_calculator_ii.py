'''
227. Basic Calculator II (Medium)
Problem Statement

Given a string s which represents an arithmetic expression, evaluate it
and return its value.

The expression contains non-negative integers and the operators + - * /,
plus spaces. There are NO parentheses.

Integer division truncates toward zero. Multiplication and division have
higher precedence than addition and subtraction.

Example
Input:
s = "3+2*2"

Output:
7
'''

def calculate(s):
    stack = []          # holds terms; sum at the end gives the answer
    number = 0          # current number being built
    op = "+"            # operator that PRECEDES `number` (default +)

    for i, ch in enumerate(s):
        if ch.isdigit():
            number = number * 10 + int(ch)

        # apply when we hit an operator or the final char (ignore spaces here)
        if (ch in "+-*/") or i == len(s) - 1:
            if op == "+":
                stack.append(number)
            elif op == "-":
                stack.append(-number)
            elif op == "*":
                stack.append(stack.pop() * number)   # high precedence: fold now
            else:  # "/"
                # truncate toward zero
                stack.append(int(stack.pop() / number))
            op = ch          # remember operator for the next number
            number = 0

    return sum(stack)


if __name__ == "__main__":
    print(calculate("3+2*2"))    # Expected: 7
    print(calculate(" 3/2 "))    # Expected: 1
    print(calculate(" 3+5 / 2 "))  # Expected: 5


'''
Pattern
✅ Stack (precedence via deferred sum)
* and / are resolved immediately against the top of the stack, while + and -
push values to be summed at the end. This handles precedence in one pass
without parentheses.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
✅ Space can be O(1) by tracking only the last number instead of a full stack,
but time stays O(n). The O(n) time is optimal.
'''
