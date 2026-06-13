'''
1. Valid Parentheses (Easy)
Problem Statement

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if open brackets are closed by the same type of bracket and in
the correct order.

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
            stack.append(c)              # opener: remember it
        else:
            # closer: top of stack must be its matching opener
            if not stack or stack.pop() != pairs[c]:
                return False

    return not stack                     # valid only if nothing left unmatched


if __name__ == "__main__":
    print(isValid("()"))        # Expected: True
    print(isValid("()[]{}"))    # Expected: True
    print(isValid("(]"))        # Expected: False
    print(isValid("([)]"))      # Expected: False

'''
Pattern
✅ Stack (brackets)
A closer must match the most recently opened bracket — LIFO order is exactly a stack.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Must read every char; nesting needs O(n) stack in the worst case.
'''
