'''
1. Subsets via Bitmask Enumeration (Medium)
Problem Statement

Given an array of distinct integers nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. The order of subsets does
not matter, so we sort the list of subsets before printing for a stable output.

Input:
nums = [1, 2, 3]

Output:
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

Explanation:
There are 2^3 = 8 subsets. Each integer mask in [0, 2^n) encodes one subset:
bit i of the mask decides whether nums[i] is included.
'''

def subsets(nums):
    n = len(nums)
    result = []
    # Iterate every integer from 0 to 2^n - 1. Each value is a "membership mask".
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            # Bit trick: (mask >> i) & 1 is 1 exactly when element i is chosen.
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    # Sort the list of subsets so the order matches the Expected output.
    print(sorted(subsets(nums)))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


'''
Pattern
✅ Subset Enumeration via Bitmask
The power set of n elements maps one-to-one to the integers [0, 2^n). Looping a
mask over that range and testing (mask >> i) & 1 lets us emit every subset
without recursion. The trick works because each bit is an independent yes/no
choice, exactly the structure of "include element i or not".

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n * 2^n)     |
| Space  | O(n * 2^n)     |

Better Possible?
❌ No
There are 2^n subsets and emitting each costs up to O(n) to build, so producing
the full power set is inherently O(n * 2^n). Backtracking has the same bound;
the bitmask form just avoids recursion overhead.
'''
