"""
2. Range Update + Range Query Fenwick (Hard)

Problem Statement
-----------------
Support BOTH range updates and range queries in O(log n) using Fenwick trees only:
  - range_update(l, r, delta): add `delta` to every element in nums[l .. r],
  - range_sum(l, r): sum of nums[l .. r].
A single BIT gives point-update / range-query. The "two-BIT trick" upgrades it to
range-update / range-query while staying O(log n) per operation.

Example
-------
Input:
  start with len-5 array of zeros: [0, 0, 0, 0, 0]
  range_update(1, 3, +2)   # -> [0, 2, 2, 2, 0]
  range_update(2, 4, +3)   # -> [0, 2, 5, 5, 3]
  range_sum(0, 4)
  range_sum(2, 3)
Output:
  15
  10
"""


class BIT:
    """Plain 1-indexed Fenwick: point update, prefix query (sum). Building block."""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):  # i is 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix(self, i):  # sum of [1..i], 1-indexed
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s


class RangeFenwick:
    """
    Two-BIT trick. Maintain B1 and B2 so that
        prefix(i) = B1.prefix(i) * i - B2.prefix(i)
    A range add of `d` over [l..r] is encoded as point updates on B1, B2 so that
    the formula above reproduces the correct prefix sums for any i.
    Derivation: range-add d on [l..r] adds, to prefix(i):
        0            if i < l
        d*(i-l+1)    if l <= i <= r
        d*(r-l+1)    if i > r
    These three piecewise-linear cases are captured by:
        B1 += d at l,        B1 -= d at r+1
        B2 += d*(l-1) at l,  B2 -= d*r at r+1
    """

    def __init__(self, n):
        self.n = n
        self.b1 = BIT(n)
        self.b2 = BIT(n)

    def _range_add(self, l, r, d):  # 1-indexed inclusive
        self.b1.update(l, d)
        self.b1.update(r + 1, -d)
        self.b2.update(l, d * (l - 1))
        self.b2.update(r + 1, -d * r)

    def _prefix(self, i):  # sum of [1..i], 1-indexed
        return self.b1.prefix(i) * i - self.b2.prefix(i)

    def range_update(self, l, r, d):
        """Add d to nums[l .. r] inclusive (0-indexed caller API)."""
        self._range_add(l + 1, r + 1, d)

    def range_sum(self, l, r):
        """Sum of nums[l .. r] inclusive (0-indexed)."""
        return self._prefix(r + 1) - self._prefix(l)


if __name__ == "__main__":
    rf = RangeFenwick(5)              # [0, 0, 0, 0, 0]
    rf.range_update(1, 3, 2)          # [0, 2, 2, 2, 0]
    rf.range_update(2, 4, 3)          # [0, 2, 5, 5, 3]
    print(rf.range_sum(0, 4))         # Expected: 15
    print(rf.range_sum(2, 3))         # Expected: 10


"""
Pattern
-------
Range-Update Range-Query Fenwick (two-BIT trick). A single BIT supports point
update + prefix query. To also support range updates we observe that a range add
makes prefix(i) a PIECEWISE-LINEAR function of i: zero before l, linear in the
interval, then constant after r. Writing prefix(i) = B1.prefix(i)*i - B2.prefix(i)
lets us encode all three regimes with O(1) point updates into two BITs. Each query
and update is two BIT operations, so still O(log n).

Use it when both updates and queries are over RANGES (e.g. add to a subarray, then
ask a subarray sum) and you prefer Fenwick's small constant over a lazy segment
tree. Works for invertible/additive operations only (sum), not min/max.

| Metric        | Value      |
|---------------|------------|
| Build         | O(n)       |
| range_sum     | O(log n)   |
| range_update  | O(log n)   |
| Space         | O(n)       |

Better Possible?
----------------
A segment tree with lazy propagation handles the same range-add + range-sum in
O(log n) and generalizes to assign / min / max, but costs ~4n space and more code.
For purely OFFLINE range updates with a single final read, a difference array is
O(1) per update and O(n) to finalize — cheaper, but it cannot answer interleaved
queries. The two-BIT Fenwick is the lightweight online choice for additive ranges.
"""
