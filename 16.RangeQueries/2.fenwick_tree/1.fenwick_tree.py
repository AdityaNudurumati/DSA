"""
1. Fenwick Tree / Binary Indexed Tree (Medium)

Problem Statement
-----------------
Implement a Fenwick Tree (Binary Indexed Tree, BIT) supporting:
  - build from an initial array `nums`,
  - point update: add a delta to a single index,
  - prefix sum: sum of nums[0 .. i],
  - range sum: sum of nums[l .. r].
All update/query operations must run in O(log n).

Example
-------
Input:
  nums = [1, 2, 3, 4, 5]
  range_sum(0, 2)   # 1 + 2 + 3
  update(1, +2)     # nums[1] becomes 4
  range_sum(0, 2)   # 1 + 4 + 3
  prefix_sum(4)     # 1 + 4 + 3 + 4 + 5
Output:
  6
  8
  17
"""


class FenwickTree:
    """1-indexed internally; the public API is 0-indexed for the caller."""

    def __init__(self, nums):
        self.n = len(nums)
        # tree[i] covers the range (i - lowbit(i), i]  (1-indexed)
        self.tree = [0] * (self.n + 1)
        # O(n) build: add each value, then push it up to its parent.
        for i, v in enumerate(nums):
            pos = i + 1
            self.tree[pos] += v
            parent = pos + (pos & -pos)
            if parent <= self.n:
                self.tree[parent] += self.tree[pos]

    def update(self, i, delta):
        """Add `delta` to nums[i] (0-indexed)."""
        i += 1  # to 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # jump to next responsible node

    def _prefix(self, i):
        """Sum of nums[0 .. i-1] for 1-indexed i (internal helper)."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)  # strip lowest set bit -> previous range
        return s

    def prefix_sum(self, i):
        """Sum of nums[0 .. i] inclusive (0-indexed i)."""
        return self._prefix(i + 1)

    def range_sum(self, l, r):
        """Sum of nums[l .. r] inclusive (0-indexed)."""
        return self._prefix(r + 1) - self._prefix(l)


if __name__ == "__main__":
    ft = FenwickTree([1, 2, 3, 4, 5])
    print(ft.range_sum(0, 2))   # Expected: 6
    ft.update(1, 2)             # nums[1]: 2 -> 4
    print(ft.range_sum(0, 2))   # Expected: 8
    print(ft.prefix_sum(4))     # Expected: 17


"""
Pattern
-------
Fenwick Tree (Binary Indexed Tree). Each node tree[i] stores the partial sum of
the range (i - lowbit(i), i], where lowbit(i) = i & (-i) isolates the lowest set
bit. Updates walk UP by adding lowbit (covering wider ranges); prefix queries walk
DOWN by stripping lowbit (chaining disjoint covering ranges). Why it works: every
prefix [1..i] decomposes into O(log n) such ranges — one per set bit of i.

Use it when you need point updates + prefix/range sums and want minimal code and
cache-friendly O(log n). For range-min/max or range updates, see segment trees /
the two-BIT trick (file 2).

| Metric        | Value      |
|---------------|------------|
| Build         | O(n)       |
| Prefix/Range  | O(log n)   |
| Point update  | O(log n)   |
| Space         | O(n)       |

Better Possible?
----------------
For pure prefix sums on a STATIC array, a prefix-sum array gives O(1) queries but
O(n) updates. Fenwick is the sweet spot when updates and queries interleave. A
segment tree matches the asymptotics but uses ~4n space and more constant factor;
Fenwick wins on simplicity for sum-like (invertible) operations.
"""
