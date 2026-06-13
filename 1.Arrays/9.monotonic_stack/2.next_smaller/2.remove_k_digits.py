'''
2. Remove K Digits (Medium)
Problem Statement

Given a string num representing a non-negative integer and an integer k, remove k
digits so the resulting number is the smallest possible. Return it as a string
(no leading zeros; "0" if empty).

Example
Input:
num = "1432219", k = 3

Output:
"1219"
'''

def removeKdigits(num, k):

    stack = []      # builds an increasing sequence of kept digits

    for d in num:
        # a kept digit larger than the current one hurts -> drop it
        while k > 0 and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)

    # if removals remain (digits were non-decreasing), trim from the end
    if k > 0:
        stack = stack[:-k]

    result = "".join(stack).lstrip("0")
    return result if result else "0"


if __name__ == "__main__":
    print(removeKdigits("1432219", 3))   # Expected: "1219"
    print(removeKdigits("10200", 1))     # Expected: "200"
    print(removeKdigits("10", 2))        # Expected: "0"

'''
Pattern
✅ Monotonic (increasing) Stack — greedy digit removal

Key Observation
A higher digit followed by a lower one should be removed first (it weighs a more
significant place). Maintain an increasing stack, popping while a budget remains.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No.
'''
