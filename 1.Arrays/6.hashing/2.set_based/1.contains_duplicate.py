'''
1. Contains Duplicate (Easy)
Problem Statement

Given an integer array nums, return True if any value appears at least twice, and
False if every element is distinct.

Example
Input:
nums = [1,2,3,1]

Output:
True
'''

def containsDuplicate(nums):

    seen = set()

    for x in nums:
        if x in seen:
            return True
        seen.add(x)

    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))   # Expected: True
    print(containsDuplicate([1, 2, 3, 4]))   # Expected: False

'''
Pattern
✅ Set membership

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
O(1) space is possible by sorting first, but that costs O(n log n) time.
'''
