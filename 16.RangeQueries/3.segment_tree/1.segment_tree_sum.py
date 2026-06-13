"""
1. Segment Tree — Range Sum + Point Update (Medium)

Problem Statement
-----------------
Given an integer array, support two operations efficiently:
  - query(l, r): return the sum of elements in the INCLUSIVE range [l, r].
  - update(i, val): set the element at index i to val.

Both operations must run in O(log n) so that interleaved queries and updates
stay fast even on large arrays.

Example
-------
Input:  arr = [1, 3, 5, 7, 9, 11]
        query(1, 3)         -> 3 + 5 + 7        = 15
        update(2, 10)       -> arr = [1,3,10,7,9,11]
        query(1, 3)         -> 3 + 10 + 7       = 20
Output: 15, 20
"""


# --- Iterative (array-backed) segment tree for range SUM ----------------------
class SegmentTreeSum:
    def __init__(self, arr):
        self.n = len(arr)
        # seg has 2*n slots: leaves live at [n, 2n), internal nodes at [1, n).
        self.seg = [0] * (2 * self.n)
        # Place leaves, then pull parents up from combined children.
        for i in range(self.n):
            self.seg[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def update(self, i, val):
        # Set leaf i = val, then recompute every ancestor.
        i += self.n
        self.seg[i] = val
        i //= 2
        while i:
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]
            i //= 2

    def query(self, l, r):
        # Sum over inclusive [l, r]; convert to half-open [l, r+1) for the loop.
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:          # l is a right child -> include it, move past.
                res += self.seg[l]
                l += 1
            if r & 1:          # r is a right child -> r-1 is in range.
                r -= 1
                res += self.seg[r]
            l //= 2
            r //= 2
        return res


if __name__ == "__main__":
    st = SegmentTreeSum([1, 3, 5, 7, 9, 11])
    print(st.query(1, 3))   # Expected: 15
    st.update(2, 10)        # set index 2 = 10
    print(st.query(1, 3))   # Expected: 20


"""
Pattern: SEGMENT TREE (iterative, array-backed)

Why this structure: a segment tree stores each array element as a leaf and each
internal node as the SUM of its two children. Any range decomposes into O(log n)
canonical node-ranges, so a query touches only O(log n) nodes. A point update
walks one root-to-leaf path, refreshing each ancestor — also O(log n).
The iterative form (leaves at index n..2n) avoids recursion overhead and uses
exactly 2n slots instead of the classic 4n.

| Metric | Value   |
|--------|---------|
| Build  | O(n)    |
| Query  | O(log n)|
| Update | O(log n)|
| Space  | O(2n)   |

Better Possible?
A Fenwick (BIT) tree also gives O(log n) sum query/update with a smaller constant
and half the memory, so for pure SUM it is the leaner choice. The segment tree
wins when the combine is not invertible (min/max/gcd) or when you later need lazy
range updates. Static arrays with no updates are better served by a prefix-sum
array (O(1) query).
"""
