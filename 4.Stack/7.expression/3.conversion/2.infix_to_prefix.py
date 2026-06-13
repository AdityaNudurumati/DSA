'''
2. Infix to Prefix (Medium)
Problem Statement

Convert an arithmetic expression written in infix notation to prefix
(Polish) notation.

Operands are single letters. Operators are + - * / and parentheses ( ).
* and / have higher precedence than + and -, and operators are
left-associative.

Trick: reverse the infix (swapping '(' and ')'), convert to postfix while
treating equal precedence as right-associative, then reverse the result.

Example
Input:
"a+b*c"

Output:
"+a*bc"
'''

def infix_to_prefix(expr):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # Step 1: reverse the expression and swap parentheses.
    reversed_expr = []
    for ch in reversed(expr):
        if ch == "(":
            reversed_expr.append(")")
        elif ch == ")":
            reversed_expr.append("(")
        else:
            reversed_expr.append(ch)

    # Step 2: convert to postfix. Because we reversed, use STRICTLY greater
    # precedence to pop (treats equal precedence as right-associative),
    # preserving correct left-associativity for the original expression.
    output = []
    stack = []
    for ch in reversed_expr:
        if ch.isalnum():
            output.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        elif ch in precedence:
            while (stack and stack[-1] != "(" and
                   precedence[stack[-1]] > precedence[ch]):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    # Step 3: reverse the postfix to get the prefix expression.
    return "".join(reversed(output))


if __name__ == "__main__":
    print(infix_to_prefix("a+b*c"))      # Expected: +a*bc
    print(infix_to_prefix("(a+b)*c"))    # Expected: *+abc


'''
Pattern
✅ Stack (Shunting-Yard on reversed expression)
Prefix is the mirror of postfix: reverse the input (swapping parens), run a
shunting-yard pass with right-associative equal-precedence handling, then
reverse the output.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Three linear passes collapse to O(n); each token is handled a constant
number of times. Optimal.
'''
