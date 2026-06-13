'''
4. Merge Sort (Medium)
Problem Statement

Sort an integer array in ascending order using Merge Sort.

Divide the array into two halves, recursively sort each, then merge the two sorted
halves into one. The merge takes the smaller front element each step, breaking ties
in favor of the left half so equal elements keep their original order (stable).

Example
Input:
nums = [5,2,8,1,9,3]

Output:
[1,2,3,5,8,9]
'''

def merge(left, right):

    merged = []
    i = j = 0
    # walk both sorted halves, taking the smaller front each time
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= keeps it stable (left wins ties)
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    # append whatever remains (only one of these is non-empty)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def mergeSort(nums):

    # 0 or 1 element is already sorted
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


if __name__ == "__main__":
    print(mergeSort([5, 2, 8, 1, 9, 3]))  # Expected: [1, 2, 3, 5, 8, 9]
    print(mergeSort([]))                   # Expected: []
    print(mergeSort([1]))                  # Expected: [1]
    print(mergeSort([3, 3, 1]))            # Expected: [1, 3, 3]

'''
Pattern
Merge Sort — divide & conquer, then stable merge.
Splitting halves gives a recursion depth of log n and each level does O(n) merge
work, so the total is O(n log n) in every case. The <= tie-break in merge makes it
stable, the property counting-sort-style algorithms rely on for multi-key sorts.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(n log n) all cases |
| Space  | O(n) for the merge   |
| Stable | Yes                  |

Better Possible?
Time is optimal for comparison sorts (Omega(n log n) lower bound). The O(n) extra
space is the trade-off; heap/quick sort are in-place but heap is unstable and quick
risks O(n^2). An in-place merge exists but is intricate and slower in practice.
'''
