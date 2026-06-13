'''
1. Next Greater Element I (Easy)
Problem Statement

You are given two arrays nums1 and nums2 where nums1 is a subset of nums2.

For each element in nums1, find the next greater element to its right in nums2.
The next greater element of a value x is the first element to the right of x in
nums2 that is strictly greater than x. If it does not exist, the answer is -1.

Return an array of the answers, one per element of nums1 (in the same order).

Example
Input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]
Output:
[-1,3,-1]
'''

def nextGreaterElement(nums1, nums2):
    # Map each value in nums2 to its next greater element.
    next_greater = {}
    stack = []                       # decreasing stack of values awaiting a greater element

    for x in nums2:
        # x is the next greater element for every smaller value on the stack.
        while stack and stack[-1] < x:
            next_greater[stack.pop()] = x
        stack.append(x)

    # Anything still on the stack has no next greater element.
    # Look up answers for nums1 (default -1).
    return [next_greater.get(v, -1) for v in nums1]


if __name__ == "__main__":
    print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))   # Expected: [-1, 3, -1]
    print(nextGreaterElement([2, 4], [1, 2, 3, 4]))       # Expected: [3, -1]


'''
Pattern
✅ Monotonic Stack (decreasing) + hash map
Scan nums2 once with a decreasing stack; when a larger value arrives it resolves
the next-greater for all smaller values waiting on the stack. A hash map lets us
answer nums1 queries in O(1) each.
| Metric | Value          |
| ------ | -------------- |
| Time   | O(n + m)       |
| Space  | O(n)           |
Better Possible?
❌ No. Every element of nums2 must be inspected once; O(n + m) is optimal.
'''
