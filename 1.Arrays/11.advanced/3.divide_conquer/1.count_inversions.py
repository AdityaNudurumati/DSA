'''
1. Count Inversions (Medium)
Problem Statement

An inversion is a pair (i, j) with i < j and arr[i] > arr[j]. Count all inversions.
(Measures how far the array is from sorted.) Must beat the naive O(n²).

Example
Input:
arr = [2,3,8,6,1]

Output:
5
Explanation:
(2,1),(3,1),(8,6),(8,1),(6,1)
'''

def countInversions(arr):

    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, lc = sort_count(a[:mid])
        right, rc = sort_count(a[mid:])
        merged, cross = merge(left, right)
        return merged, lc + rc + cross

    def merge(left, right):
        result = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                # left[i] > right[j]: left[i..] all form inversions with right[j]
                result.append(right[j])
                j += 1
                inv += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    _, total = sort_count(arr)
    return total


if __name__ == "__main__":
    print(countInversions([2, 3, 8, 6, 1]))   # Expected: 5
    print(countInversions([1, 2, 3, 4, 5]))   # Expected: 0
    print(countInversions([5, 4, 3, 2, 1]))   # Expected: 10

'''
Pattern
✅ Merge Sort with cross-pair counting

Key Observation
During the merge, when a right element is placed before remaining left elements,
all of those left elements are inversions with it -> add (len(left) - i).

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No (comparison-based lower bound).
'''
