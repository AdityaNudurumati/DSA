'''
3. Merge K Sorted Arrays (Medium)
Problem Statement

Given k sorted arrays, merge them into one sorted array.

(Same idea merges k sorted linked lists.)

Example
Input:
arrays = [[1,4,5],[1,3,4],[2,6]]

Output:
[1,1,2,3,4,4,5,6]
'''

import heapq

def mergeKSortedArrays(arrays):

    # heap entries: (value, which array, index within that array)
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(arrays[i]):              # push the next item from that array
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

    return result


if __name__ == "__main__":
    print(mergeKSortedArrays([[1, 4, 5], [1, 3, 4], [2, 6]]))
    # Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    print(mergeKSortedArrays([[], [1], []]))   # Expected: [1]

'''
Pattern
✅ Min-heap of the k front elements

Key Observation
The next smallest overall is always among the current fronts of the k arrays. A
heap of size k yields it in O(log k); refill from the array it came from.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(N log k)     | (N = total elements)
| Space  | O(k)           |

Better Possible?
❌ No. (Pairwise merging is O(N log k) too but with more overhead.)
'''
