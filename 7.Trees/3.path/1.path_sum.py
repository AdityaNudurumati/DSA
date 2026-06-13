"""
112. Path Sum (Easy)

Problem Statement:
Given the root of a binary tree and an integer targetSum, return True if the
tree has a root-to-leaf path such that adding up all the values along the path
equals targetSum. A leaf is a node with no children.

Example:
    Input:  root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
    Output: True        (5 -> 4 -> 11 -> 2 sums to 22)

    Input:  root = [1,2,3], targetSum = 5
    Output: False
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


def level_order(root):
    """Root -> list of level-by-level value lists (for verification)."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        out.append(level)
    return out


def has_path_sum(root, target):
    # Top-down: subtract node value as we descend; check remainder at a leaf.
    if not root:
        return False
    if not root.left and not root.right:        # leaf
        return root.val == target
    rem = target - root.val
    return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)


if __name__ == "__main__":
    t1 = build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(has_path_sum(t1, 22))   # Expected: True

    t2 = build([1, 2, 3])
    print(has_path_sum(t2, 5))    # Expected: False


"""
Pattern: PATH-BASED (Root -> Leaf)
Technique: top-down DFS, carrying the remaining target down each branch and
checking it only at leaves. We pass info DOWN (remaining sum) instead of
combining bottom-up, because membership of a single root-to-leaf path is a
purely downward question.

| Metric | Value |
| Time   | O(n)  — each node visited once |
| Space  | O(h)  — recursion stack, h = tree height |

Better Possible?
O(n) time is optimal (must potentially inspect every node). Space can drop to
O(1) extra with Morris-style traversal, but at a large clarity cost — not worth
it for an interview answer.
"""
