'''
3. Intersection of Two Arrays (Easy)
Problem Statement

Given two integer arrays nums1 and nums2, return their intersection: each element
in the result must be unique. The result may be in any order.

Example
Input:
nums1 = [4,9,5], nums2 = [9,4,9,8,4]

Output:
[4,9]   (any order)
'''

def intersection(nums1, nums2):

    # set intersection gives the unique common elements directly
    common = set(nums1) & set(nums2)
    return sorted(common)      # sorted only to make the demo output deterministic


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))           # Expected: [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))     # Expected: [4, 9]

'''
Pattern
✅ Set intersection

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + m)       |
| Space  | O(n + m)       |

Better Possible?
❌ No. (sorted() here is just for a stable printout, not required.)
'''
