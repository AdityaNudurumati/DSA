'''
47. Permutations II (Medium)
Problem Statement

Given a collection of numbers, nums, that might contain duplicates, return all
possible unique permutations in any order.

Example:
Input:
nums = [1,1,2]

Output:
[[1,1,2], [1,2,1], [2,1,1]]
'''


def permuteUnique(nums):
    nums.sort()                           # group duplicates together
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # skip a duplicate whose identical predecessor is unused at this level
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(sorted(permuteUnique(nums)))
    # Expected: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]


'''
Pattern
✅ Backtracking with duplicate pruning
Sort, then within a branch skip nums[i] when it equals nums[i-1] and the
predecessor is unused, ensuring each set of equal values is placed in order.
| Metric | Value     |
| ------ | --------- |
| Time   | O(n * n!) |
| Space  | O(n)      |
Better Possible?
❌ No

Unique permutations can still approach n!; pruning only removes duplicates.
'''
