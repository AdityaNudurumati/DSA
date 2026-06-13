"""
2. Range Max Query — Segment Tree + Point Update (Medium)

Problem Statement
-----------------
Given an integer array, support two operations efficiently:
  - query(l, r): return the MAXIMUM element in the INCLUSIVE range [l, r].
  - update(i, val): set the element at index i to val.

Both operations must run in O(log n).

Example
-------
Input:  arr = [1, 3, 2, 7, 9, 11]
        query(1, 3)         -> max(3, 2, 7)      = 7
        update(4, 1)        -> arr = [1,3,2,7,1,11]
        query(3, 5)         -> max(7, 1, 11)     = 11
Output: 7, 11
"""


# --- Iterative (array-backed) segment tree for range MAX ----------------------
# Identity for max is -infinity, so an empty/untouched slot never wins a compare.
NEG_INF = float("-inf")


class SegmentTreeMax:
    def __init__(self, arr):
        self.n = len(arr)
        # Leaves at [n, 2n); internal nodes at [1, n) hold the max of children.
        self.seg = [NEG_INF] * (2 * self.n)
        for i in range(self.n):
            self.seg[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = max(self.seg[2 * i], self.seg[2 * i + 1])

    def update(self, i, val):
        # Set leaf i = val, then re-max every ancestor on the path to the root.
        i += self.n
        self.seg[i] = val
        i //= 2
        while i:
            self.seg[i] = max(self.seg[2 * i], self.seg[2 * i + 1])
            i //= 2

    def query(self, l, r):
        # Max over inclusive [l, r]; treat as half-open [l, r+1).
        res = NEG_INF
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.seg[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.seg[r])
            l //= 2
            r //= 2
        return res


if __name__ == "__main__":
    st = SegmentTreeMax([1, 3, 2, 7, 9, 11])
    print(st.query(1, 3))   # Expected: 7
    st.update(4, 1)         # set index 4 = 1
    print(st.query(3, 5))   # Expected: 11


"""
Pattern: SEGMENT TREE (iterative, array-backed) with a MAX combine

Why this structure: identical skeleton to the sum tree, but each internal node
stores max(left, right) and the query identity is -infinity. Range max is an
IDEMPOTENT, associative operation, so the same O(log n) range-decomposition and
point-update logic applies — only the combine function changes.

| Metric | Value   |
|--------|---------|
| Build  | O(n)    |
| Query  | O(log n)|
| Update | O(log n)|
| Space  | O(2n)   |

Better Possible?
For a STATIC array (no updates) a Sparse Table answers range-max in O(1) after
O(n log n) preprocessing, beating the segment tree's O(log n) query. But max is
not invertible, so a Fenwick tree cannot do arbitrary range-max with point
DECREASES — the segment tree is the right tool once updates are required. Range
UPDATES would additionally need lazy propagation (pattern 4).
"""
