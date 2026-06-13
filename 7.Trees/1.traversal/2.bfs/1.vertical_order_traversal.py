'''
987. Vertical Order Traversal of a Binary Tree (Hard)
Problem Statement

Given the root of a binary tree, calculate the vertical order traversal.

For each node at position (row, col), its left child is at (row+1, col-1) and
its right child is at (row+1, col+1). The root is at (0, 0).

The vertical order traversal lists nodes column by column, from leftmost column
to rightmost. Within a column, nodes are ordered by row (top to bottom). If two
nodes share the same row AND column, they are ordered by value (ascending).

Return a list of lists, one inner list per column.

Example 1:
Input:  root = [3,9,20,None,None,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input:  root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
        (5 and 6 share (row=2, col=0) -> ordered by value: 5 then 6)
'''

from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Build a tree from a LEVEL-ORDER list (None = missing node).
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
    return root


def level_order(root):
    # Verification helper: BFS list of values (skips Nones).
    out, q = [], deque([root] if root else [])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def verticalTraversal(root):
    # DFS collecting (col -> list of (row, val)); then sort.
    cols = defaultdict(list)

    def dfs(node, row, col):
        if not node:
            return
        cols[col].append((row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    out = []
    # Columns left -> right; within a column sort by (row, value).
    for col in sorted(cols):
        col_vals = [val for row, val in sorted(cols[col])]
        out.append(col_vals)
    return out


if __name__ == "__main__":
    root1 = build([3, 9, 20, None, None, 15, 7])
    print(verticalTraversal(root1))  # Expected: [[9], [3, 15], [20], [7]]

    root2 = build([1, 2, 3, 4, 5, 6, 7])
    print(verticalTraversal(root2))  # Expected: [[4], [2], [1, 5, 6], [3], [7]]

    root3 = build([])
    print(verticalTraversal(root3))  # Expected: []


'''
Pattern
✅ BFS/DFS + Coordinate Sort
Assign every node a (row, col) coordinate, bucket by column, then sort. The
tie-break rule (same row AND col -> ascending value) is why a plain BFS that
relies on traversal order is NOT enough — we must explicitly sort by
(row, value) inside each column. DFS or BFS both work since we sort afterward.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |   (sorting the buckets dominates)
| Space  | O(n)       |   (coordinate map + recursion/queue)

Better Possible?
❌ The value tie-break forces a comparison sort within columns, so O(n log n)
is the bound here. Without the same-cell value ordering rule, a BFS with a
min/max column counter would give O(n); the ordering requirement is what
pushes it to log-linear.
'''
