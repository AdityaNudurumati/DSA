"""
3. Bottom View of Binary Tree (Medium)

Problem Statement:
Given the root of a binary tree, return the BOTTOM VIEW: the set of nodes visible
when the tree is viewed from directly below. For each horizontal column (distance
from root, left = -1, right = +1) the LAST node encountered in a top-down BFS is
visible. Output the visible values ordered left column -> right column.

Example:
    Input:  root = [1,2,3,4,5,6,7]
    Output: [4,2,6,3,7]
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


def bottom_view(root):
    # BFS with column index; ALWAYS overwrite so the LAST value per column wins.
    if not root:
        return []
    col = {}                              # column -> last node val (bottom-most)
    q = deque([(root, 0)])
    while q:
        node, c = q.popleft()
        col[c] = node.val                 # overwrite => last seen in column survives
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    return [col[c] for c in sorted(col)]


if __name__ == "__main__":
    # Build tree [1,2,3,4,5,6,7]
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7
    # column 0 holds 1 (top) then 5 then 6; 6 is dequeued last => bottom wins.
    root = build([1, 2, 3, 4, 5, 6, 7])
    print(bottom_view(root))  # Expected: [4, 2, 6, 3, 7]


"""
Pattern: Tree Views — Vertical column bookkeeping over a BFS.
Technique: identical to top view BUT overwrite the column entry on every visit so
the LAST node reached per column (lowest in a top-down BFS) survives. Emit by
sorted column.
Why overwrite: BFS proceeds level by level top-down; the final write to a column
corresponds to the deepest / last-in-reading-order node, which is what an observer
below sees. For ties in a column on the same level, the later (right-most in BFS
order) node wins, matching the conventional bottom-view definition.

| Metric | Value          |
|--------|----------------|
| Time   | O(n log n)     |  (sort of distinct columns)
| Space  | O(n)           |

Better Possible?
Same as top view: track min/max column and use an array to drop the sort for O(n)
time. With <= n keys the sort is negligible, so the dict version stays preferred.
"""
