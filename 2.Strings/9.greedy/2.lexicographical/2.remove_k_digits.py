'''
2. Remove K Digits (Medium)
Problem Statement

Given a non-negative integer represented as a string num, remove exactly k
digits so that the resulting number is the smallest possible.

Return it as a string (no leading zeros, and "0" if everything is removed).

Example
Input:  num = "1432219", k = 3
Output: "1219"

Input:  num = "10200", k = 1
Output: "200"

Input:  num = "10", k = 2
Output: "0"
'''


def removeKdigits(num, k):
    stack = []  # builds an increasing-as-possible digit sequence

    for d in num:
        # Greedy: a bigger digit to the left of a smaller one hurts the value,
        # so pop it while we still have removals (k) to spend.
        while k > 0 and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)

    # If removals remain, the sequence is non-decreasing -> drop from the end.
    if k > 0:
        stack = stack[:-k]

    # Strip leading zeros; empty result means the number is 0.
    result = "".join(stack).lstrip("0")
    return result if result else "0"


if __name__ == "__main__":
    print(removeKdigits("1432219", 3))  # Expected: 1219
    print(removeKdigits("10200", 1))    # Expected: 200
    print(removeKdigits("10", 2))       # Expected: 0


'''
Pattern
✅ Increasing Monotonic Stack (Greedy Lexicographical)
Pop a larger digit before a smaller one whenever a removal is available; this
minimizes the leading digits, which dominate the value.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |
Better Possible?
❌ No. Every digit is pushed/popped once; linear time is optimal.
'''
