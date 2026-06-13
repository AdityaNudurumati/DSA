'''
1. Relative Sort Array (Easy)
Problem Statement

Given two arrays arr1 and arr2 where all elements of arr2 are distinct and every
element of arr2 also appears in arr1, sort arr1 so that its elements follow the
relative order given by arr2. Elements of arr1 that do not appear in arr2 are
placed at the end in ascending order.

Example
Input:
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

Output:
[2,2,2,1,4,3,3,9,6,7,19]
'''

def relativeSortArray(arr1, arr2):

    # rank[v] = position of v in arr2 (its priority); smaller goes first
    rank = {v: i for i, v in enumerate(arr2)}
    n = len(arr2)

    # custom key: known values use their arr2 rank;
    # unknown values get rank n (after all known) then sort by value ascending.
    # second key (value) only matters for the unknown group but is harmless for known
    # since each known rank is unique.
    def key(v):
        return (rank.get(v, n), v)

    # sort by hand-built key (algorithm here is the KEY, not the sort)
    return sorted(arr1, key=key)


if __name__ == "__main__":
    print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
    # Expected: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
    # Expected: [22, 28, 8, 6, 17, 44]

'''
Pattern
✅ Custom Sorting — derive a (priority, value) key from a reference order

Algorithm & Why
Build a rank map from arr2 so each "known" element gets a small index. Sort arr1
by the tuple (rank, value): known elements order by their arr2 position; unknown
elements share rank n (pushed to the end) and break ties by ascending value. A
single stable key-sort captures both rules at once.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(n log n)        |
| Space  | O(n)              |
| Stable | Yes (Timsort key) |

Better Possible?
✅ Counting sort over the bounded value range (0..1000 in the original constraints)
gives O(n + k) without comparisons, but the key-sort is clearer and general.
'''
