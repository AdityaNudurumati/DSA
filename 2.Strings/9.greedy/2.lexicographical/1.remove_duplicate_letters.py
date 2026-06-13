'''
1. Remove Duplicate Letters / Smallest Subsequence of Distinct Characters (Medium)
Problem Statement

Given a string s, remove duplicate letters so that every letter appears exactly
once. Among all such results, return the lexicographically smallest one.

Example
Input:  s = "bcabc"
Output: "abc"

Input:  s = "cbacdcbc"
Output: "acdb"
'''


def removeDuplicateLetters(s):
    last = {ch: i for i, ch in enumerate(s)}  # last index each char appears
    stack = []          # builds an increasing (smallest) subsequence
    in_stack = set()    # chars currently on the stack

    for i, ch in enumerate(s):
        if ch in in_stack:
            continue  # each letter only once; skip if already chosen
        # Greedy: pop bigger chars on top if they reappear later, so a smaller
        # char can take an earlier position.
        while stack and stack[-1] > ch and last[stack[-1]] > i:
            in_stack.remove(stack.pop())
        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)


if __name__ == "__main__":
    print(removeDuplicateLetters("bcabc"))     # Expected: abc
    print(removeDuplicateLetters("cbacdcbc"))  # Expected: acdb


'''
Pattern
✅ Increasing Monotonic Stack (Greedy Lexicographical)
Keep an increasing stack; pop a larger char on top only when it appears again
later, guaranteeing the smallest distinct subsequence.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
(O(1) extra: stack and set bounded by 26 letters)
Better Possible?
❌ No. Each char is pushed and popped at most once -> linear is optimal.
'''
