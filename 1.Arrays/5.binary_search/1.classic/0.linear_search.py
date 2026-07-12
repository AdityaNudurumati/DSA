'''
0. Linear Search (Easy)
Problem Statement

Given an array nums (sorted OR unsorted) and a target, return the index of the
first occurrence of target, or -1 if it is not present. This is the baseline
O(n) search that binary search improves upon when the array is sorted.

Example
Input:
nums = [4, 2, 7, 1, 9, 3], target = 9

Output:
4
'''

def linearSearch(nums, target):

    # walk every element left to right; return the first match
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


if __name__ == "__main__":
    print(linearSearch([4, 2, 7, 1, 9, 3], 9))   # Expected: 4
    print(linearSearch([4, 2, 7, 1, 9, 3], 5))   # Expected: -1
    print(linearSearch([], 1))                    # Expected: -1
    print(linearSearch([8], 8))                   # Expected: 0

'''
Pattern
Linear Search — scan every element until a match is found.
Works on ANY array (no sorting required). It is the O(n) baseline; when the
array is sorted, Binary Search (see 1.binary_search.py) does it in O(log n).

| Metric | Value                                   |
| ------ | --------------------------------------- |
| Time   | O(n) worst/avg, O(1) best (first slot)  |
| Space  | O(1)                                    |

Better Possible?
On an UNSORTED array, no — you may have to look at every element, so O(n) is
optimal. On a SORTED array, Binary Search beats it at O(log n).
'''
