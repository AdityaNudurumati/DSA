'''
46. Permutations (Medium)
Problem Statement

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example:
Input:
nums = [1,2,3]

Output:
[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
'''


def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):        # goal: full-length arrangement
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:                   # each element used once per branch
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(sorted(permute(nums)))
    # Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


'''
Pattern
✅ Backtracking (pick an unused element each step)
A used[] mask tracks which elements are already in the current path; we recurse
until the path holds all n elements.
| Metric | Value    |
| ------ | -------- |
| Time   | O(n * n!) |
| Space  | O(n)     |
Better Possible?
❌ No

There are n! permutations and copying each costs O(n); O(n * n!) is optimal.
'''
