'''
1. Infix to Postfix (Medium)
Problem Statement

Convert an arithmetic expression written in infix notation to postfix
(Reverse Polish) notation using the shunting-yard algorithm.

Operands are single letters. Operators are + - * / and parentheses ( ).
* and / have higher precedence than + and -. All operators are
left-associative.

Example
Input:
"a+b*c"

Output:
"abc*+"
'''

def infix_to_postfix(expr):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    output = []          # builds the postfix string (operands + popped ops)
    stack = []           # operator / parenthesis stack

    for ch in expr:
        if ch.isalnum():
            output.append(ch)                 # operand goes straight to output
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            # pop until the matching '('
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()                        # discard '('
        elif ch in precedence:
            # pop operators of higher/equal precedence (left-associative)
            while (stack and stack[-1] != "(" and
                   precedence[stack[-1]] >= precedence[ch]):
                output.append(stack.pop())
            stack.append(ch)
        # spaces ignored

    while stack:                               # flush remaining operators
        output.append(stack.pop())

    return "".join(output)


if __name__ == "__main__":
    print(infix_to_postfix("a+b*c"))         # Expected: abc*+
    print(infix_to_postfix("(a+b)*c-d"))     # Expected: ab+c*d-


'''
Pattern
✅ Stack (Shunting-Yard)
Operators wait on a stack until an operator of lower precedence (or end of a
group) forces them out, which reorders infix into postfix in a single pass.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Each token is pushed/popped at most once; O(n) is optimal.
'''
