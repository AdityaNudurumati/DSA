'''
224. Basic Calculator (Hard)
Problem Statement

Given a string s representing a valid expression, evaluate it and return its value.

The expression contains only non-negative integers, the operators + and -,
parentheses ( ), and spaces. There is no * or /.

Example
Input:
s = "(1+(4+5+2)-3)+(6+8)"

Output:
23
'''

def calculate(s):
    result = 0          # running total of the current level
    number = 0          # current number being built
    sign = 1            # +1 or -1, sign applied to `number`
    stack = []          # saves (result, sign) when entering '('

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)   # build multi-digit number
        elif ch == "+":
            result += sign * number          # commit pending number
            number = 0
            sign = 1
        elif ch == "-":
            result += sign * number
            number = 0
            sign = -1
        elif ch == "(":
            # push context, start a fresh sub-expression
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * number          # finish inner expression
            number = 0
            result *= stack.pop()            # multiply by sign before '('
            result += stack.pop()            # add the outer result
        # spaces are ignored

    return result + sign * number            # commit any trailing number


if __name__ == "__main__":
    print(calculate("1 + 1"))                  # Expected: 2
    print(calculate(" 2-1 + 2 "))              # Expected: 3
    print(calculate("(1+(4+5+2)-3)+(6+8)"))    # Expected: 23


'''
Pattern
✅ Stack (defer outer context across parentheses)
Without * /, we only need a running sum with a sign. Parentheses are handled
by pushing the outer result and sign onto a stack, evaluating the inner block,
then folding it back in.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Single linear scan; the stack depth is bounded by parenthesis nesting. Optimal.
'''
