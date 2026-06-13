'''
77. Combinations (Medium)
Problem Statement

Given two integers n and k, return all possible combinations of k numbers
chosen from the range [1, n].

You may return the answer in any order.

Example:
Input:
n = 4, k = 2

Output:
[[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
'''


def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:                # goal: chose k numbers
            result.append(path[:])
            return
        # prune: stop if not enough numbers remain to reach length k
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(i + 1, path)        # i+1 -> each number used once
            path.pop()

    backtrack(1, [])
    return result


if __name__ == "__main__":
    n, k = 4, 2
    print(sorted(combine(n, k)))
    # Expected: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


'''
Pattern
✅ Backtracking over a start index
Advance a start pointer so numbers are only chosen forward (no reuse, no
reordering); a length pruning bound skips branches too short to finish.
| Metric | Value       |
| ------ | ----------- |
| Time   | O(k * C(n,k)) |
| Space  | O(k)        |
Better Possible?
❌ No

There are C(n,k) combinations, each copied in O(k); that is optimal.
'''
