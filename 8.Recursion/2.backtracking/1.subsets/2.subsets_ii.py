'''
90. Subsets II (Medium)
Problem Statement

Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Example:
Input:
nums = [1,2,2]

Output:
[[], [1], [1,2], [1,2,2], [2], [2,2]]
'''


def subsetsWithDup(nums):
    nums.sort()                           # group duplicates together
    result = []

    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            # skip a duplicate value at the same tree depth
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(sorted(subsetsWithDup(nums)))
    # Expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]


'''
Pattern
✅ Backtracking with duplicate pruning
Sort first so equal values are adjacent, then at each depth skip the second+
occurrence (i > start and nums[i] == nums[i-1]) to avoid duplicate subsets.
| Metric | Value      |
| ------ | ---------- |
| Time   | O(n * 2^n) |
| Space  | O(n)       |
Better Possible?
❌ No

Output can still be up to 2^n subsets; pruning only removes duplicates.
'''
