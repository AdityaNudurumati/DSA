"""
113. Path Sum II (Medium)

Problem Statement:
Given the root of a binary tree and an integer targetSum, return all
root-to-leaf paths where the sum of the node values in the path equals
targetSum. Each path should be returned as a list of node values.
A leaf is a node with no children.

Example:
    Input:  root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
    Output: [[5,4,11,2],[5,8,4,5]]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node, LeetCode style) -> root."""
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


def path_sum(root, target):
    res, path = [], []

    def dfs(node, rem):
        if not node:
            return
        path.append(node.val)
        rem -= node.val
        if not node.left and not node.right and rem == 0:   # qualifying leaf
            res.append(path[:])                             # copy current path
        else:
            dfs(node.left, rem)
            dfs(node.right, rem)
        path.pop()                                          # backtrack

    dfs(root, target)
    return res


if __name__ == "__main__":
    t = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(path_sum(t, 22))   # Expected: [[5, 4, 11, 2], [5, 8, 4, 5]]


"""
Pattern: PATH-BASED (Root -> Leaf, enumerate)
Technique: top-down DFS with backtracking. We push the node onto a running
`path`, recurse, then pop on the way out so siblings reuse a single buffer.
A copy of `path` is snapshotted only when a leaf hits the exact target.

| Metric | Value |
| Time   | O(n^2) worst — n nodes, and copying a path costs up to O(n) |
| Space  | O(h) for the recursion/path buffer (output excluded) |

Better Possible?
The O(n^2) ceiling comes from materializing every qualifying path, which is
inherent to the output. Time is optimal relative to output size.
"""
