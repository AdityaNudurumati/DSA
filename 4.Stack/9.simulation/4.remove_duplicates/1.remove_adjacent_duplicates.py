'''
1. Remove All Adjacent Duplicates In String (Easy)
Problem Statement

Given a string of lowercase letters, repeatedly remove two adjacent and equal letters until
no such pair remains, then return the final string. The answer is guaranteed to be unique.

Example
Input:
s = "abbaca"

Output:
"ca"
'''

def removeDuplicates(s):

    stack = []      # characters with no pending adjacent duplicate

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()          # current cancels the identical top
        else:
            stack.append(ch)     # no match -> keep it

    return "".join(stack)


if __name__ == "__main__":
    print(removeDuplicates("abbaca"))   # Expected: ca
    print(removeDuplicates("azxxzy"))   # Expected: ay

'''
Pattern
✅ Stack Simulation — push; pop when the incoming item cancels the top

Key Observation
Adjacent-duplicate removal can cascade (removing one pair exposes a new pair). A stack tracks
the current reduced string: if the next character equals the top, the pair annihilates;
otherwise it is pushed. One pass handles every cascade.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
