'''
5. Merge Sorted Array (Easy)
Problem Statement

You are given two sorted integer arrays nums1 and nums2.

nums1 has length m + n: the first m slots hold its values, the last n slots are 0
placeholders. nums2 has n values.

Merge nums2 into nums1 so nums1 becomes one sorted array. Do it in-place.

Example
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output:
[1,2,2,3,5,6]
'''

def merge(nums1, m, nums2, n):

    i = m - 1            # last real value in nums1
    j = n - 1            # last value in nums2
    k = m + n - 1        # last slot in nums1

    # Fill from the back so we never overwrite unread values.
    while j >= 0:

        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # Expected: [1, 2, 2, 3, 5, 6]

'''
Pattern
✅ Two Pointers, filling from the back

Key Observation
Merging front-to-back would overwrite unread nums1 values. Starting from the
largest end avoids that and needs no extra array.

| Metric | Value |
| ------ | ----- |
| Time   | O(m + n) |
| Space  | O(1)     |

Better Possible?
❌ No. Must touch every element.
'''
