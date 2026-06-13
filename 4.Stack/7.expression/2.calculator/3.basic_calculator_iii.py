'''
772. Basic Calculator III (Hard)
Problem Statement

Implement a basic calculator to evaluate a simple expression string.

The expression contains non-negative integers, the operators + - * /,
parentheses ( ), and spaces.

Integer division truncates toward zero. * and / have higher precedence than
+ and -, and parentheses override precedence.

Example
Input:
s = "2*(5+5*2)/3+(6/2+8)"

Output:
21
'''

def calculate(s):

    def helper(it):
        # Evaluate one parenthesis level, consuming from iterator `it`.
        stack = []
        number = 0
        op = "+"          # operator preceding `number`

        while True:
            ch = next(it, None)

            if ch is not None and ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == "(":
                # a parenthesised group acts as a single operand
                number = helper(it)
            elif ch is None or ch in "+-*/)":
                # commit `number` under the previous operator
                if op == "+":
                    stack.append(number)
                elif op == "-":
                    stack.append(-number)
                elif op == "*":
                    stack.append(stack.pop() * number)
                else:  # "/"
                    stack.append(int(stack.pop() / number))  # trunc toward zero

                number = 0
                op = ch
                # end of this level (close paren or end of string)
                if ch is None or ch == ")":
                    break
            # spaces ignored

        return sum(stack)

    return helper(iter(s))


if __name__ == "__main__":
    print(calculate("1+1"))                       # Expected: 2
    print(calculate("6-4/2"))                      # Expected: 4
    print(calculate("2*(5+5*2)/3+(6/2+8)"))        # Expected: 21


'''
Pattern
✅ Stack + Recursion (precedence with parentheses)
Each parenthesis level is evaluated by the same routine as Calculator II
(stack-based precedence). A '(' recurses to produce a single operand value,
so nesting is handled cleanly by the recursion stack.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Every character is read once; recursion/stack depth is bounded by
nesting. O(n) is optimal.
'''
