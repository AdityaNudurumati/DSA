'''
1. Next Greater Element I (Easy)
Problem Statement

nums1 is a subset of nums2. For each value in nums1, find the next greater element
to its right in nums2. If none exists, use -1. Return the answers in nums1's order.

Example
Input:
nums1 = [4,1,2], nums2 = [1,3,4,2]

Output:
[-1,3,-1]
'''

def nextGreaterElement(nums1, nums2):

    next_greater = {}       # value -> its next greater element in nums2
    stack = []              # decreasing stack of values awaiting their NGE

    for x in nums2:
        while stack and stack[-1] < x:
            next_greater[stack.pop()] = x
        stack.append(x)

    return [next_greater.get(x, -1) for x in nums1]


if __name__ == "__main__":
    print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))   # Expected: [-1, 3, -1]
    print(nextGreaterElement([2, 4], [1, 2, 3, 4]))       # Expected: [3, -1]

'''
Pattern
✅ Monotonic (decreasing) Stack + hashmap

Key Observation
Scan nums2 once; when the current value exceeds the stack top, it IS that top's next
greater. Store every answer in a map, then read off nums1.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Each element pushed/popped once.
'''
