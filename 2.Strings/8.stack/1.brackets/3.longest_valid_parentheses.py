'''
3. Longest Valid Parentheses (Hard)
Problem Statement

Given a string containing just the characters '(' and ')', return the length of the
longest valid (well-formed) parentheses substring.

Example
Input:
s = ")()())"

Output:
4

Explanation:
The longest valid substring is "()()", with length 4.
'''

def longestValidParentheses(s):

    # Stack holds indices. Seed with -1 to act as a "base" boundary so the
    # length of a valid run = current_index - index_below_the_matched_open.
    stack = [-1]
    best = 0

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)            # push index of every open paren
        else:
            stack.pop()                # try to match this ')' with a '('
            if stack:
                # valid run reaches back to the new top (a boundary index)
                best = max(best, i - stack[-1])
            else:
                # no opener to match: this ')' becomes the new boundary
                stack.append(i)

    return best


if __name__ == "__main__":
    print(longestValidParentheses("(()"))     # Expected: 2
    print(longestValidParentheses(")()())"))   # Expected: 4
    print(longestValidParentheses(""))         # Expected: 0

'''
Pattern
✅ Stack of indices (boundary trick)
Push indices; on a match measure distance to the last unmatched boundary. The
sentinel -1 lets a run starting at index 0 be measured uniformly.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
✅ Space can be reduced to O(1) with a two-pass left/right counter scan, but the
stack version is the canonical single-pass solution.
'''
