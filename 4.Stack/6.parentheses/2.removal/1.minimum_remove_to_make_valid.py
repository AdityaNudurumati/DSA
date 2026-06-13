'''
1. Minimum Remove to Make Valid Parentheses (Medium)
Problem Statement

Given a string s of '(' , ')' and lowercase English letters, remove the minimum
number of parentheses ( '(' or ')' , in any positions ) so the resulting string is
valid, and return any valid result. A string is valid when it is empty, contains
only letters, or every bracket has a correct matching partner.

Example
Input:
s = "lee(t(c)o)de)"

Output:
"lee(t(c)o)de"
'''

def minRemoveToMakeValid(s):

    chars = list(s)
    stack = []                      # indices of currently unmatched '('

    for i, c in enumerate(chars):
        if c == '(':
            stack.append(i)         # remember this open bracket
        elif c == ')':
            if stack:
                stack.pop()         # matched with a previous '('
            else:
                chars[i] = ''       # unmatched ')' -> mark for removal

    # any '(' still on the stack never got matched -> remove them
    for i in stack:
        chars[i] = ''

    return "".join(chars)


if __name__ == "__main__":
    print(minRemoveToMakeValid("lee(t(c)o)de)"))  # Expected: "lee(t(c)o)de"
    print(minRemoveToMakeValid("a)b(c)d"))         # Expected: "ab(c)d"
    print(minRemoveToMakeValid("))(("))            # Expected: ""

'''
Pattern
✅ Stack of indices — flag unmatched brackets, then rebuild

Key Observation
A ')' is invalid the moment it appears with no open bracket waiting; a '(' is
invalid if it is still unmatched at the end. Recording open-bracket indices on a
stack lets us pinpoint exactly the minimal set of brackets to drop.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — every character is visited once and the removals are provably minimal.
'''
