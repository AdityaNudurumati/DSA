'''
1. Merge Sort Tree (Hard)
Problem Statement

You are given a static array arr. Answer many queries of the form:
"How many elements in the index range [l, r] are STRICTLY GREATER than k?"

A Merge Sort Tree is a segment tree where each node stores the SORTED
subarray it covers. A node's sorted list is the merge of its two children's
sorted lists (exactly the intermediate state of a merge sort, hence the name).
To count elements > k in a node fully inside [l, r], binary-search the node's
sorted list. Summing over the O(log n) nodes that tile [l, r] gives the answer.

Input:
arr = [1, 5, 2, 8, 3]
count_greater(0, 4, 3)   # elements > 3 in the whole array -> {5, 8} = 2
count_greater(1, 3, 4)   # elements > 4 in [5, 2, 8]       -> {5, 8} = 2
count_greater(0, 4, 0)   # elements > 0 in whole array     -> all 5

Output:
2
2
5
'''

import bisect


class MergeSortTree:
    # Each tree[node] holds the sorted subarray for the range that node covers.
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [[] for _ in range(4 * self.n)]
        if self.n:
            self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, lo, hi):
        if lo == hi:
            self.tree[node] = [arr[lo]]          # leaf: single-element sorted list
            return
        mid = (lo + hi) // 2
        left, right = 2 * node, 2 * node + 1
        self._build(arr, left, lo, mid)
        self._build(arr, right, mid + 1, hi)
        # merge the two sorted child lists (the merge step of merge sort)
        self.tree[node] = self._merge(self.tree[left], self.tree[right])

    @staticmethod
    def _merge(a, b):
        merged = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    def count_greater(self, l, r, k):
        # public API: count indices in [l, r] whose value > k
        return self._query(1, 0, self.n - 1, l, r, k)

    def _query(self, node, lo, hi, l, r, k):
        if r < lo or hi < l:                     # no overlap
            return 0
        if l <= lo and hi <= r:                  # node fully inside query range
            sorted_vals = self.tree[node]
            # number of values > k = total - (count of values <= k)
            return len(sorted_vals) - bisect.bisect_right(sorted_vals, k)
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r, k)
                + self._query(2 * node + 1, mid + 1, hi, l, r, k))


if __name__ == "__main__":
    arr = [1, 5, 2, 8, 3]
    mst = MergeSortTree(arr)

    print(mst.count_greater(0, 4, 3))   # Expected: 2
    print(mst.count_greater(1, 3, 4))   # Expected: 2
    print(mst.count_greater(0, 4, 0))   # Expected: 5


'''
Pattern
Merge Sort Tree = segment tree whose every node stores its subarray sorted.
Why: a "count of values relating to k inside an index range" query can't be
answered by a plain sum/min segment tree, but if each node keeps its values
sorted we can binary-search the threshold k inside each of the O(log n) nodes
that cover the range. The build is literally a merge sort that keeps every
intermediate merged list, so total stored values = O(n log n).

| Metric | Value          |
| ------ | -------------- |
| Build  | O(n log n)     |
| Query  | O(log^2 n)     |  (log n nodes, each a log n binary search)
| Update | O(n) / unsuited|  (sorted lists make point update expensive)
| Space  | O(n log n)     |

Better Possible?
For this OFFLINE static problem, a wavelet tree or Mo's algorithm with an order
statistic structure can reach O(log n) or O((n+q)sqrt(n)) per query, and merge
sort tree query can be cut to O(log n) with fractional cascading. But for a
clean, by-hand, std-lib-only solution, O(log^2 n) per query is the standard and
practically optimal choice. Updates, however, are not supported well.
'''
