'''
307. Range Sum Query - Mutable (Medium)  -- Fenwick / BIT version
Problem Statement

Given an integer array nums, support:
  1. update(index, val)    set nums[index] = val.
  2. sumRange(left, right)  sum of nums[left..right] inclusive.

Solve it with a Binary Indexed Tree (Fenwick tree) instead of a segment tree.

Implement the NumArray class:
  - NumArray(nums)
  - update(index, val)
  - sumRange(left, right)

Example
Input:
  nums = [1, 3, 5]
  sumRange(0, 2)   -> 9
  update(1, 2)
  sumRange(0, 2)   -> 8
'''

from collections import deque


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


def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


# ---- Solution: Fenwick / Binary Indexed Tree (1-indexed) ----
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = [0] * self.n           # keep a copy to compute deltas
        self.bit = [0] * (self.n + 1)      # 1-indexed tree
        for i, v in enumerate(nums):
            self.update(i, v)

    def _add(self, i, delta):
        # i is 1-indexed; add delta along the BIT path.
        while i <= self.n:
            self.bit[i] += delta
            i += i & (-i)

    def _prefix(self, i):
        # Sum of nums[0..i-1]; i is 1-indexed prefix length.
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def update(self, index, val):
        # Apply only the delta so the tree stays consistent.
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left, right):
        # Inclusive [left, right] = prefix(right+1) - prefix(left).
        return self._prefix(right + 1) - self._prefix(left)


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print(na.sumRange(0, 2))   # Expected: 9
    na.update(1, 2)
    print(na.sumRange(0, 2))   # Expected: 8

    # Helpers demo:
    print(level_order(build([1, 3, 5])))  # Expected: [1, 3, 5]

'''
Pattern
Fenwick Tree / Binary Indexed Tree (prefix sums with point update)

Technique & why
A BIT stores partial sums indexed by the lowest set bit: bit[i] covers the
range (i - (i&-i), i]. Walking i += i&-i moves to the next responsible node when
updating; i -= i&-i jumps over already-counted blocks when summing a prefix.
Range sum = prefix(right+1) - prefix(left). We store a copy of nums so update
can apply the delta (val - old) rather than re-inserting. This gives the same
O(log n) bounds as a segment tree with about half the array and far less code.

| Metric    | Value    |
| --------- | -------- |
| Build     | O(n log n) (or O(n) with a linear build) |
| update    | O(log n) |
| sumRange  | O(log n) |
| Space     | O(n)     |

Better Possible?
The asymptotics match a segment tree; the constant factor is smaller. For pure
mutable prefix/range sums this is the standard optimal choice. A segment tree is
only "better" when you need operations a BIT cannot do directly (range min/max,
lazy range updates).
'''
