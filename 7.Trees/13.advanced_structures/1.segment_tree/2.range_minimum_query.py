'''
Range Minimum Query (Medium)
Problem Statement

Given a static array arr, answer many queries of the form query(l, r): return the
minimum value among arr[l..r] inclusive. Preprocess so each query is fast.

Implement a segment tree that supports:
  - RMQ(arr)        build the tree from arr.
  - query(l, r)     minimum of arr[l..r] inclusive.

Example
Input:
  arr = [1, 3, 2, 7, 9, 11]
  query(1, 3)  -> 2     # min(3, 2, 7)
  query(0, 5)  -> 1     # min of whole array
  query(2, 4)  -> 2     # min(2, 7, 9)
'''

from collections import deque
import math


# ---- Minimal TreeNode + helpers (required by repo convention) ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing node, LeetCode style) -> root.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q, i = deque([root]), 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return root


def inorder(root):
    # Inorder values for verification.
    out, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


# ---- Solution: recursive segment tree (min) ----
class RMQ:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        # Safe size: 2 * next-power-of-two >= n covers all internal nodes.
        size = 1 if self.n == 0 else 1 << (self.n - 1).bit_length()
        self.tree = [math.inf] * (2 * size)
        if self.n:
            self._build(1, 0, self.n - 1)

    def _build(self, node, lo, hi):
        if lo == hi:
            self.tree[node] = self.arr[lo]
            return self.tree[node]
        mid = (lo + hi) // 2
        left = self._build(2 * node, lo, mid)
        right = self._build(2 * node + 1, mid + 1, hi)
        self.tree[node] = min(left, right)
        return self.tree[node]

    def query(self, l, r):
        # Public: minimum over inclusive [l, r].
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, lo, hi, l, r):
        if r < lo or hi < l:          # no overlap
            return math.inf
        if l <= lo and hi <= r:       # total overlap -> cached answer
            return self.tree[node]
        mid = (lo + hi) // 2          # partial overlap -> recurse
        return min(self._query(2 * node, lo, mid, l, r),
                   self._query(2 * node + 1, mid + 1, hi, l, r))


if __name__ == "__main__":
    rmq = RMQ([1, 3, 2, 7, 9, 11])
    print(rmq.query(1, 3))   # Expected: 2
    print(rmq.query(0, 5))   # Expected: 1
    print(rmq.query(2, 4))   # Expected: 2

    # Helpers demo (build a level-order BST-ish tree, print inorder):
    print(inorder(build([2, 1, 3])))  # Expected: [1, 2, 3]

'''
Pattern
Segment Tree (recursive, node = min of its segment)

Technique & why
Each node owns a contiguous segment [lo, hi] and caches the minimum of that
segment; children split it in half. A query is classified per node as no-overlap
(ignore), total-overlap (return cached min directly), or partial-overlap (recurse
both children). Because a query range decomposes into O(log n) total-overlap
segments, each query is O(log n) after an O(n) build.

| Metric   | Value    |
| -------- | -------- |
| Build    | O(n)     |
| query    | O(log n) |
| Space    | O(n)     |

Better Possible?
For a purely static array, a Sparse Table answers each min query in O(1) after
O(n log n) preprocessing. The segment tree is preferred when point updates are
also needed (updates would be O(log n) here, impossible in O(1) for a sparse
table). So this is optimal for the mutable / general case.
'''
