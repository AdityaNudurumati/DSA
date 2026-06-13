'''
1. Valid Parentheses (Easy)
Problem Statement

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. A string is valid when every opening
bracket is closed by the same type of bracket and in the correct order.

Example
Input:
s = "()[]{}"

Output:
True
'''

def isValid(s):

    pairs = {')': '(', ']': '[', '}': '{'}   # closer -> matching opener
    stack = []

    for c in s:
        if c in '([{':
            stack.append(c)                  # open bracket -> remember it
        else:
            # closer must match the most recent open bracket
            if not stack or stack.pop() != pairs[c]:
                return False

    return not stack                         # leftover opens => invalid


if __name__ == "__main__":
    print(isValid("()"))      # Expected: True
    print(isValid("()[]{}"))  # Expected: True
    print(isValid("(]"))      # Expected: False
    print(isValid("([)]"))    # Expected: False

'''
Pattern
✅ Stack — push opens, pop+match on closes

Key Observation
Brackets close in last-in-first-out order, so a stack naturally enforces correct
nesting: each closer must pair with the top (most recent) opener.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — every character must be examined and nesting state must be tracked.
'''
