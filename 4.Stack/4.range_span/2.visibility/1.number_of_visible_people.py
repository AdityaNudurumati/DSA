'''
1. Number of Visible People in a Queue (Hard)
Problem Statement

There are n people in a queue, numbered left to right. You are given an array
heights of distinct integers where heights[i] is the height of the i-th person.

A person i can see another person j to their right (i < j) if every person
between them is strictly shorter than both of them; formally, person i can see
person j when:
    min(heights[i], heights[j]) > max(heights[i+1], ..., heights[j-1]).

Return an array answer where answer[i] is the number of people the i-th person
can see to their right.

Example
Input:
heights = [10, 6, 8, 5, 11, 9]

Output:
[3, 1, 2, 1, 1, 0]
Explanation:
Person 0 (10) sees 6, 8, 11 -> 3
Person 1 (6)  sees 8        -> 1
Person 2 (8)  sees 5, 11    -> 2
Person 3 (5)  sees 11       -> 1
Person 4 (11) sees 9        -> 1
Person 5 (9)  sees nobody   -> 0

Input:
heights = [5, 1, 2, 3, 10]

Output:
[4, 1, 1, 1, 0]
'''

def canSeePersonsCount(heights):
    n = len(heights)
    answer = [0] * n
    # Monotonic decreasing stack of heights to the right, scanning right->left.
    stack = []

    for i in range(n - 1, -1, -1):
        h = heights[i]
        # Everyone shorter than h is visible to person i, but blocks anyone
        # further right, so pop them and count each.
        while stack and stack[-1] < h:
            stack.pop()
            answer[i] += 1
        # If a taller person remains, person i sees them too (then is blocked).
        if stack:
            answer[i] += 1
        stack.append(h)

    return answer


if __name__ == "__main__":
    print(canSeePersonsCount([10, 6, 8, 5, 11, 9]))
    # Expected: [3, 1, 2, 1, 1, 0]
    print(canSeePersonsCount([5, 1, 2, 3, 10]))
    # Expected: [4, 1, 1, 1, 0]


'''
Pattern
✅ Monotonic Decreasing Stack (right-to-left)

Why: Scanning from the right, the stack holds the candidates a person could see.
A person sees every shorter person before them (each gets popped and counted),
plus the first taller person who stops their view. Maintaining a decreasing
stack means each person is pushed and popped once → linear, versus O(n^2) for
checking every pair.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No

Each person is pushed/popped once; O(n) is optimal.
'''
