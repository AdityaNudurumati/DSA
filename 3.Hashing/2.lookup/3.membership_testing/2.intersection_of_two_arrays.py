'''
2. Intersection of Two Arrays (Easy)
Problem Statement

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique, and the result may be in any order.

Example
Input:  nums1 = [1, 2, 2, 1], nums2 = [2, 2]            -> [2]
        nums1 = [4, 9, 5],    nums2 = [9, 4, 9, 8, 4]   -> [4, 9]
'''

def intersection(nums1, nums2):

    set1 = set(nums1)                       # set for O(1) membership testing
    result = set()
    for x in nums2:                         # keep values of nums2 that also live in set1
        if x in set1:
            result.add(x)                   # set guarantees uniqueness automatically
    return list(result)


if __name__ == "__main__":
    print(sorted(intersection([1, 2, 2, 1], [2, 2])))          # Expected: [2]
    print(sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])))    # Expected: [4, 9]

'''
Pattern
✅ Membership Testing (build a set, probe it for shared elements)

Key Observation
Convert one array to a set, then scan the other testing membership in O(1). Collecting
hits in a set drops duplicates for free, so the answer is naturally unique.

| Metric | Value |
| ------ | ----- |
| Time   | O(n + m) |
| Space  | O(n)     |

Better Possible?
❌ Every element of both arrays must be touched once, so O(n + m) is optimal. Sorting
both and merging is O(n log n + m log m) and uses no extra hash, but is slower.
'''
