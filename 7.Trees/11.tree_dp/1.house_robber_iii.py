'''
1. House Robber III (Medium)
Problem Statement

The thief has found himself a new place for his thievery: a binary tree of houses.
The root is the entrance. Besides the root, each house has exactly one parent house.
After a tour, the thief realized that all houses form a binary tree.

It will automatically contact the police if two DIRECTLY-LINKED houses (a parent and
its child) are both robbed on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can
rob WITHOUT alerting the police.

Example
Input:
root = [3,2,3,None,3,None,1]
        3
       / \
      2   3
       \   \
        3   1
Output:
7
Explanation:
Rob 3 (root) + 3 + 1 = 7.

Input:
root = [3,4,5,1,3,None,1]
        3
       / \
      4   5
     / \   \
    1   3   1
Output:
9
Explanation:
Rob 4 + 5 = 9.
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node, LeetCode style) -> root
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):                 # left child
            if values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
        if i < len(values):                 # right child
            if values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
    return root


def level_order(root):
    # flatten to a plain list of values, skipping None placeholders
    out = []
    q = deque([root]) if root else deque()
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def rob(root):
    # each node returns (rob_this, skip_this)
    #   rob  = node.val + skip(left) + skip(right)   # children must be skipped
    #   skip = max(left states) + max(right states)  # children free to choose
    def dfs(node):
        if not node:
            return (0, 0)
        l = dfs(node.left)
        r = dfs(node.right)
        rob_here = node.val + l[1] + r[1]
        skip_here = max(l) + max(r)
        return (rob_here, skip_here)

    return max(dfs(root))


if __name__ == "__main__":
    root1 = build([3, 2, 3, None, 3, None, 1])
    print(level_order(root1))   # Expected: [3, 2, 3, 3, 1]
    print(rob(root1))           # Expected: 7

    root2 = build([3, 4, 5, 1, 3, None, 1])
    print(level_order(root2))   # Expected: [3, 4, 5, 1, 3, 1]
    print(rob(root2))           # Expected: 9


'''
Pattern
Tree DP — include / exclude (rob / skip) per node, bottom-up.

Technique & why
Each node has two mutually-exclusive choices: rob it (then its children CANNOT be
robbed) or skip it (children are free to take their own best). A single post-order
pass returns the tuple (rob_here, skip_here); the parent combines child tuples in
O(1). This avoids the exponential blow-up of recomputing overlapping subtrees that a
naive "try every subset" recursion would incur — every subtree is visited once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack, h = tree height)

Better Possible?
No. Every node must be inspected at least once, so O(n) time is optimal; space is
the unavoidable recursion depth O(h).
'''
