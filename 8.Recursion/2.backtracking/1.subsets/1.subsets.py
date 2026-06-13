'''
78. Subsets (Medium)
Problem Statement

Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Example:
Input:
nums = [1,2,3]

Output:
[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
'''


def subsets(nums):
    result = []

    def backtrack(start, path):
        # every node on the decision tree is a valid subset
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])          # choose
            backtrack(i + 1, path)        # explore (no reuse -> i+1)
            path.pop()                    # un-choose

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    # sort so the list-of-lists order is deterministic
    print(sorted(subsets(nums)))
    # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


'''
Pattern
✅ Backtracking (take / skip via start index)
At each index we explore including nums[i] then exclude it; recording the path
at every node yields all 2^n subsets without duplicates.
| Metric | Value      |
| ------ | ---------- |
| Time   | O(n * 2^n) |
| Space  | O(n)       |
Better Possible?
❌ No

There are 2^n subsets and each costs O(n) to copy, so O(n * 2^n) is optimal.
'''
