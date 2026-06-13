'''
1. Remove All Adjacent Duplicates In String (Easy)
Problem Statement

You are given a string s of lowercase letters. A duplicate removal consists of
choosing two adjacent and equal letters and removing them.

Repeatedly make duplicate removals on s until no more can be made, then return the
final string. The answer is guaranteed to be unique.

Example
Input:
s = "abbaca"

Output:
"ca"

Explanation:
"abbaca" -> remove "bb" -> "aaca" -> remove "aa" -> "ca".
'''

def removeDuplicates(s):

    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()          # top equals current: they cancel out
        else:
            stack.append(c)      # otherwise keep it

    return ''.join(stack)


if __name__ == "__main__":
    print(removeDuplicates("abbaca"))   # Expected: ca
    print(removeDuplicates("azxxzy"))   # Expected: ay

'''
Pattern
✅ Stack (cancel adjacent equal items)
A new char cancels the top if equal; otherwise it is pushed. The stack always
holds the partially-reduced string.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Each char is pushed/popped at most once; output itself can be O(n).
'''
