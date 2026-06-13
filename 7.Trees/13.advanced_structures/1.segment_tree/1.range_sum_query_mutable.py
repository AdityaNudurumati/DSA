'''
307. Range Sum Query - Mutable (Medium)
Problem Statement

Given an integer array nums, handle multiple queries of the following types:
  1. Update the value of an element in nums.
  2. Calculate the sum of the elements of nums between indices left and right
     inclusive where left <= right.

Implement the NumArray class:
  - NumArray(nums)        initialises the object with the array nums.
  - update(index, val)    updates nums[index] to be val.
  - sumRange(left, right) returns the sum of nums[left..right] inclusive.

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
    # Level-order values for verification.
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


# ---- Solution: array-backed segment tree (sum) ----
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        # tree[1..2n-1]: leaves stored at [n, 2n), internal nodes below.
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        # Set leaf then bubble the change up to the root.
        i = index + self.n
        self.tree[i] = val
        i //= 2
        while i >= 1:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def sumRange(self, left, right):
        # Inclusive [left, right]; walk leaves inward accumulating sums.
        lo, hi, s = left + self.n, right + self.n + 1, 0
        while lo < hi:
            if lo & 1:
                s += self.tree[lo]; lo += 1
            if hi & 1:
                hi -= 1; s += self.tree[hi]
            lo //= 2; hi //= 2
        return s


if __name__ == "__main__":
    na = NumArray([1, 3, 5])
    print(na.sumRange(0, 2))   # Expected: 9
    na.update(1, 2)
    print(na.sumRange(0, 2))   # Expected: 8

    # Helpers demo (build a level-order tree, print it):
    print(level_order(build([1, 3, 5])))  # Expected: [1, 3, 5]

'''
Pattern
Segment Tree (array / iterative "bottom-up" layout)

Technique & why
Store the array's values in leaves [n, 2n) of a flat array; each internal node
i caches the sum of its two children (2i, 2i+1). A point update touches one leaf
and the O(log n) ancestors on the path to the root. A range query walks the two
boundary leaves inward, absorbing whole sub-trees that are fully inside the
range. This beats a naive O(n)-per-query approach when updates and queries are
interleaved many times.

| Metric          | Value    |
| --------------- | -------- |
| Build           | O(n)     |
| update          | O(log n) |
| sumRange        | O(log n) |
| Space           | O(n)     |

Better Possible?
A Fenwick/BIT (see ../2.fenwick_tree/1.range_sum_bit.py) gives the same
O(log n) bounds with a smaller constant and less code for pure prefix sums.
Segment trees are strictly more general (min/max/gcd, lazy range updates), so
this is optimal for the general mutable-range-query problem.
'''
