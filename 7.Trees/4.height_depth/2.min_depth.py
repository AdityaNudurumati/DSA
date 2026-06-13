"""
111. Minimum Depth of Binary Tree (Easy)

Problem Statement:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest LEAF node. A leaf is a node with no children.

Note: a node with only one child is NOT a leaf, so the empty side must be
ignored when computing the minimum.

Example:
    Input:  root = [3,9,20,None,None,15,7]
    Output: 2
    Input:  root = [2,None,3,None,4]
    Output: 3
    (LeetCode-style level-order: 2's right child is 3, 3's right child is 4,
     a 3-node right-leaning chain, so the only leaf sits at depth 3. Note: the
     well-known LC example that yields 4 is the longer chain
     [2,None,3,None,4,None,5].)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Build a tree from a LeetCode-style level-order list (None = missing)."""
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
    """Return values grouped per level (for verification)."""
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out


def min_depth(root):
    # Bottom-up recursion, but a one-child node must not count the missing side.
    if not root:
        return 0
    # If one child is absent, the shortest path must go through the present one.
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


if __name__ == "__main__":
    print(min_depth(build([3, 9, 20, None, None, 15, 7])))  # Expected: 2
    print(min_depth(build([2, None, 3, None, 4])))          # Expected: 3
    print(min_depth(build([2, None, 3, None, 4, None, 5])))  # Expected: 4

    print(min_depth(build([])))   # Expected: 0
    print(min_depth(build([1])))  # Expected: 1


"""
Pattern: Height / Depth / Diameter.
Technique: bottom-up recursion with a leaf guard. The subtle point separating
this from max_depth: a node with a single child is not a leaf, so taking a
plain min(left, right) would wrongly return 0 from the empty side and stop
short of an actual leaf. We therefore recurse only into present children when
one side is missing.

| Metric | Value |
| Time   | O(n)  |  worst case visits every node
| Space  | O(h)  |  recursion stack (O(n) worst, O(log n) balanced)

Better Possible?
A BFS variant can return early at the FIRST leaf encountered, which is faster
on average (it need not explore deep subtrees once a shallow leaf is found),
but worst-case time stays O(n). Asymptotically optimal either way.
"""
