'''
1. Lazy Range Add + Range Sum (Medium)
Problem Statement

Maintain an integer array and support two operations efficiently:
  range_add(l, r, v) -> add v to every element in [l, r]
  range_sum(l, r)    -> return the sum of elements in [l, r]
Both must run in O(log n) by deferring (lazy) the pending additions.

Example
Input:
arr = [0, 0, 0, 0, 0]
range_add(0, 2, 5)
range_add(1, 4, 3)
range_sum(0, 4) -> 27
range_sum(1, 3) -> 19
'''


class LazySegmentTree:
    """Segment tree with lazy propagation for range-add / range-sum."""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)   # subtree sums
        self.lazy = [0] * (4 * n)   # pending +v to push down

    def _apply(self, node, lo, hi, v):
        # add v to every element of [lo, hi] covered by node
        self.tree[node] += v * (hi - lo + 1)
        self.lazy[node] += v

    def _push_down(self, node, lo, hi):
        if self.lazy[node]:
            mid = (lo + hi) // 2
            self._apply(2 * node, lo, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, hi, self.lazy[node])
            self.lazy[node] = 0

    def _update(self, node, lo, hi, l, r, v):
        if r < lo or hi < l:            # no overlap
            return
        if l <= lo and hi <= r:         # total overlap
            self._apply(node, lo, hi, v)
            return
        self._push_down(node, lo, hi)   # partial overlap
        mid = (lo + hi) // 2
        self._update(2 * node, lo, mid, l, r, v)
        self._update(2 * node + 1, mid + 1, hi, l, r, v)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:            # no overlap
            return 0
        if l <= lo and hi <= r:         # total overlap
            return self.tree[node]
        self._push_down(node, lo, hi)   # partial overlap
        mid = (lo + hi) // 2
        return (self._query(2 * node, lo, mid, l, r) +
                self._query(2 * node + 1, mid + 1, hi, l, r))

    def range_add(self, l, r, v):
        self._update(1, 0, self.n - 1, l, r, v)

    def range_sum(self, l, r):
        return self._query(1, 0, self.n - 1, l, r)


if __name__ == "__main__":
    st = LazySegmentTree(5)             # [0, 0, 0, 0, 0]
    st.range_add(0, 2, 5)              # [5, 5, 5, 0, 0]
    st.range_add(1, 4, 3)             # [5, 8, 8, 3, 3]
    print(st.range_sum(0, 4))         # Expected: 27
    print(st.range_sum(1, 3))         # Expected: 19

'''
Pattern
✅ Lazy Propagation Segment Tree (range add, range sum)

Each node stores the sum of its segment plus a lazy tag holding additions not yet
pushed to children. On total overlap we apply the tag to the node only; on partial
overlap we push the tag down first, then recurse. This is why range update stays
O(log n) instead of O(n).

| Metric       | Value     |
| ------------ | --------- |
| Build        | O(n)      |
| Range Query  | O(log n)  |
| Range Update | O(log n)  |
| Space        | O(4n)     |

Better Possible?
❌ Not for arbitrary interleaved range-add + range-sum. A Fenwick range-update /
range-query variant matches O(log n) but a plain prefix/difference array cannot do
both online.
'''
