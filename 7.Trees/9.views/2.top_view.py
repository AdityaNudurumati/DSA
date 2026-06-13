"""
2. Top View of Binary Tree (Medium)

Problem Statement:
Given the root of a binary tree, return the TOP VIEW: the set of nodes visible
when the tree is viewed from directly above. For each horizontal column (distance
from root, left = -1, right = +1) only the FIRST node encountered in a top-down
BFS is visible. Output the visible values ordered left column -> right column.

Example:
    Input:  root = [1,2,3,4,5,6,7]
    Output: [4,2,1,3,7]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing node, LeetCode style) -> root.
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        node = q[0]
        if node.left is None and v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        elif node.left is not None:
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root


def level_order(root):
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


def top_view(root):
    # BFS with column index; keep only the FIRST value seen per column.
    if not root:
        return []
    col = {}                              # column -> first node val (top-most)
    q = deque([(root, 0)])
    while q:
        node, c = q.popleft()
        if c not in col:                  # first time we hit this column = visible
            col[c] = node.val
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    # Order columns left -> right.
    return [col[c] for c in sorted(col)]


if __name__ == "__main__":
    # Build tree [1,2,3,4,5,6,7]
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7
    # columns: 4@-2  2@-1  1@0  3@+1  7@+2  (5,6 sit at col 0 but 1 came first)
    root = build([1, 2, 3, 4, 5, 6, 7])
    print(top_view(root))  # Expected: [4, 2, 1, 3, 7]


"""
Pattern: Tree Views — Vertical column bookkeeping over a BFS.
Technique: BFS carrying a horizontal distance (column) per node; the first node
reached in each column (BFS guarantees top-down, level by level) is what shows in
the top view. Store first value per column in a dict, then emit by sorted column.
Why BFS not DFS: a top-down BFS guarantees the first node seen in a column is the
highest one; a naive DFS could reach a lower node first and overwrite incorrectly.

| Metric | Value          |
|--------|----------------|
| Time   | O(n log n)     |  (sort of distinct columns)
| Space  | O(n)           |

Better Possible?
The sort can be dropped to O(n) by tracking min/max column and writing into an
array indexed by (column - min_col); time then O(n). Sorting a dict of <= n keys
is negligible in practice, so the dict approach is the common, clear choice.
"""
