'''
2. Persistent Segment Tree (Hard)
Problem Statement

You are given a static array arr. Answer many queries of the form:
"What is the k-th SMALLEST value (1-indexed) among the elements in index
range [l, r]?"

Build n+1 versions of a segment tree over the VALUE domain (after coordinate
compression). Version i is built from version i-1 by inserting arr[i-1], which
creates only O(log n) new nodes and shares all the rest -> "persistent".
The frequency of values in index range [l, r] is exactly
   version[r+1] - version[l]
computed node-by-node as we descend. Walk down: if the left value-subtree of
this difference holds >= k elements go left, else subtract and go right.

Input:
arr = [1, 5, 2, 6, 3, 7, 4]
kth_smallest(0, 6, 1)   # 1st smallest of whole array -> 1
kth_smallest(0, 6, 4)   # 4th smallest of whole array -> 4
kth_smallest(2, 4, 2)   # values [2, 6, 3], 2nd smallest -> 3

Output:
1
4
3
'''

import bisect


class Node:
    __slots__ = ("left", "right", "count")
    def __init__(self, left=None, right=None, count=0):
        self.left = left          # child Node (shared across versions)
        self.right = right
        self.count = count        # how many array elements fall in this value range


class PersistentSegmentTree:
    def __init__(self, arr):
        # coordinate-compress values -> indices 0..m-1 in the value tree
        self.sorted_vals = sorted(set(arr))
        self.m = len(self.sorted_vals)
        empty = self._build(0, self.m - 1)        # version 0: empty tree
        self.versions = [empty]
        for x in arr:
            vi = bisect.bisect_left(self.sorted_vals, x)   # compressed index
            new_root = self._insert(self.versions[-1], 0, self.m - 1, vi)
            self.versions.append(new_root)

    def _build(self, lo, hi):
        if lo == hi:
            return Node(count=0)
        mid = (lo + hi) // 2
        return Node(self._build(lo, mid), self._build(mid + 1, hi), 0)

    def _insert(self, prev, lo, hi, pos):
        # create a new node copying prev, incrementing the path to leaf 'pos'
        if lo == hi:
            return Node(count=prev.count + 1)
        mid = (lo + hi) // 2
        if pos <= mid:
            new_left = self._insert(prev.left, lo, mid, pos)
            return Node(new_left, prev.right, prev.count + 1)
        else:
            new_right = self._insert(prev.right, mid + 1, hi, pos)
            return Node(prev.left, new_right, prev.count + 1)

    def kth_smallest(self, l, r, k):
        # difference of versions [l, r] inclusive -> version[r+1] minus version[l]
        return self._query(self.versions[l], self.versions[r + 1], 0, self.m - 1, k)

    def _query(self, vlo, vhi, lo, hi, k):
        if lo == hi:
            return self.sorted_vals[lo]
        mid = (lo + hi) // 2
        # elements in the left value-half within this index range
        left_count = vhi.left.count - vlo.left.count
        if k <= left_count:
            return self._query(vlo.left, vhi.left, lo, mid, k)
        else:
            return self._query(vlo.right, vhi.right, mid + 1, hi, k - left_count)


if __name__ == "__main__":
    arr = [1, 5, 2, 6, 3, 7, 4]
    pst = PersistentSegmentTree(arr)

    print(pst.kth_smallest(0, 6, 1))   # Expected: 1
    print(pst.kth_smallest(0, 6, 4))   # Expected: 4
    print(pst.kth_smallest(2, 4, 2))   # Expected: 3


'''
Pattern
Persistent Segment Tree (a.k.a. functional segment tree) keeps every historical
version while sharing unchanged nodes. Building version i over the VALUE domain
from version i-1 inserts arr[i-1] and only clones the O(log n) nodes on the root
-> leaf path. Because counts are additive, the multiset of values appearing in
index range [l, r] is the node-wise subtraction version[r+1] - version[l]; a
single descent (go left while the left subtree's differential count >= k) finds
the k-th smallest.

| Metric        | Value      |
| ------------- | ---------- |
| Build         | O(n log n) |
| Query (k-th)  | O(log n)   |
| Point insert  | O(log n)   |
| Space         | O(n log n) |

Better Possible?
O(log n) per k-th-in-range query is essentially optimal for the online setting,
and matches a wavelet tree (which uses less memory). For a purely OFFLINE batch
of queries, Mo's algorithm or merge-sort-tree + binary search also works but is
slower per query. So persistent segment tree is the optimal online choice.
'''
