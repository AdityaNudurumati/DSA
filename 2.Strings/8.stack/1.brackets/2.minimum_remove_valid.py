'''
2. Minimum Remove to Make Valid Parentheses (Medium)
Problem Statement

Given a string s of '(' , ')' and lowercase English letters, remove the minimum
number of parentheses ('(' or ')') so the resulting string is valid, and return it.

A string is valid if every '(' has a matching ')' and they are correctly ordered.

Example
Input:
s = "lee(t(c)o)de)"

Output:
"lee(t(c)o)de"
'''

def minRemoveToMakeValid(s):

    chars = list(s)
    stack = []                       # indices of '(' still waiting for a match

    for i, c in enumerate(chars):
        if c == '(':
            stack.append(i)          # remember position of this open paren
        elif c == ')':
            if stack:
                stack.pop()          # matched with a pending '('
            else:
                chars[i] = ''        # unmatched ')': mark for removal

    # any '(' still on the stack never got matched -> remove them too
    for i in stack:
        chars[i] = ''

    return ''.join(chars)


if __name__ == "__main__":
    print(minRemoveToMakeValid("lee(t(c)o)de)"))  # Expected: lee(t(c)o)de
    print(minRemoveToMakeValid("a)b(c)d"))         # Expected: ab(c)d
    print(minRemoveToMakeValid("))(("))            # Expected:

'''
Pattern
✅ Stack (track unmatched bracket positions)
Stack holds indices of open parens; unmatched closers are removed on sight, and
any opens left on the stack at the end are removed too.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No on time. Space can drop to O(1) extra with two passes + counters, but O(n)
is the clearest formulation.
'''
