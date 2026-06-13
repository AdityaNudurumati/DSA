'''
2. Longest Valid Parentheses (Hard)
Problem Statement

Given a string s containing just the characters '(' and ')', find the length of
the longest valid (well-formed) contiguous parentheses substring.

Example
Input:
s = ")()())"

Output:
4
'''

def longestValidParentheses(s):

    # Stack holds indices of UNMATCHED chars. Seed with -1 as a base
    # "last invalid position" so a valid run length = i - stack[-1].
    stack = [-1]
    best = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)            # push index of an open bracket
        else:
            stack.pop()                # try to match with an open bracket
            if stack:
                # current top is the last unmatched index before this run
                best = max(best, i - stack[-1])
            else:
                # this ')' is unmatched -> it becomes the new base
                stack.append(i)

    return best


if __name__ == "__main__":
    print(longestValidParentheses("(()"))     # Expected: 2
    print(longestValidParentheses(")()())"))   # Expected: 4
    print(longestValidParentheses(""))         # Expected: 0

'''
Pattern
✅ Stack of indices — track valid spans via last unmatched position

Key Observation
Keeping indices (not characters) lets us measure a valid run as the distance from
the current index to the last unmatched boundary on the stack. Seeding the stack
with -1 handles runs that start at index 0.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
✅ Yes on space — a two-pass left/right counter scan solves it in O(1) space,
   but the stack approach is the clearest single-pass solution.
'''
