'''
2. Lazy Range Assign + Range Sum (Medium)
Problem Statement

Maintain an integer array and support:
  range_assign(l, r, v) -> set every element in [l, r] to v
  range_sum(l, r)       -> return the sum of elements in [l, r]
Assignment overwrites, so the lazy tag must distinguish "no pending assign" from a
real pending value (including 0). Both operations run in O(log n).

Example
Input:
arr = [1, 1, 1, 1, 1]
range_assign(1, 3, 5)
range_sum(0, 4) -> 17
range_assign(0, 2, 2)
range_sum(0, 4) -> 12
'''


class LazyAssignTree:
    """Segment tree with lazy propagation for range-assign / range-sum."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        # None means "no pending assignment"; any number (even 0) is a real tag
        self.lazy = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1, arr)

    def _build(self, node, lo, hi, arr):
        if lo == hi:
            self.tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid, arr)
        self._build(2 * node + 1, mid + 1, hi, arr)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _apply(self, node, lo, hi, v):
        # assign v to every element of [lo, hi] covered by node
        self.tree[node] = v * (hi - lo + 1)
        self.lazy[node] = v

    def _push_down(self, node, lo, hi):
        if self.lazy[node] is not None:
            mid = (lo + hi) // 2
            self._apply(2 * node, lo, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, hi, self.lazy[node])
            self.lazy[node] = None

    def _update(self, node, lo, hi, l, r, v):
        if r < lo or hi < l:
            return
        if l <= lo and hi <= r:
            self._apply(node, lo, hi, v)
            return
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, l, r, v)
        self._update(2 * node + 1, mid + 1, hi, l, r, v)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:
            return 0
        if l <= lo and hi <= r:
            return self.tree[node]
        self._push_down(node, lo, hi)
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r) +
                self._query(2 * node + 1, mid + 1, hi, l, r))

    def range_assign(self, l, r, v):
        self._update(1, 0, self.n - 1, l, r, v)

    def range_sum(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    st = LazyAssignTree([1, 1, 1, 1, 1])
    st.range_assign(1, 3, 5)           # [1, 5, 5, 5, 1]
    print(st.range_sum(0, 4))          # Expected: 17
    st.range_assign(0, 2, 2)           # [2, 2, 2, 5, 1]
    print(st.range_sum(0, 4))          # Expected: 12

'''
Pattern
✅ Lazy Propagation Segment Tree (range assign, range sum)

Like range-add, but the lazy tag is an overwrite, not an increment. The newest
assignment wins, so pushing a parent's tag down simply replaces the child's tag.
The tag uses None as a sentinel so that assigning the value 0 is still recognized
as a real pending operation.

| Metric       | Value     |
| ------------ | --------- |
| Build        | O(n)      |
| Range Query  | O(log n)  |
| Range Update | O(log n)  |
| Space        | O(4n)     |

Better Possible?
❌ Not for online range-assign + range-sum. Difference arrays do not compose with
overwrite semantics; the lazy segment tree is the standard O(log n) answer.
'''
