'''
101. Symmetric Tree (Easy)
Problem Statement

Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
symmetric around its center).

Example:
Input:  root = [1,2,2,3,4,4,3]
Output: True

Input:  root = [1,2,2,null,3,null,3]
Output: False

Explanation:
        1                 1
       / \               / \
      2   2             2   2
     / \ / \             \   \
    3  4 4  3             3    3
The first tree mirrors perfectly; the second has both extra children on the right,
breaking the mirror.
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Build a tree from a LeetCode-style level-order list (None = missing node).
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            v = values[i]; i += 1
            if v is not None:
                node.left = TreeNode(v); q.append(node.left)
        if i < len(values):
            v = values[i]; i += 1
            if v is not None:
                node.right = TreeNode(v); q.append(node.right)
    return root


def level_order(root):
    # Standard BFS listing (helper for verification).
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


def isSymmetric(root):
    # BOTTOM-UP on a PAIR of nodes: each mirrored pair returns its verdict upward.
    def mirror(a, b):
        if not a and not b:
            return True                    # base: both empty -> mirrored
        if not a or not b or a.val != b.val:
            return False                   # shape/value mismatch -> not mirrored
        # combine: outer pair (a.left vs b.right) AND inner pair (a.right vs b.left)
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    if not root:
        return True
    return mirror(root.left, root.right)


if __name__ == "__main__":
    print(isSymmetric(build([1, 2, 2, 3, 4, 4, 3])))            # Expected: True

    print(isSymmetric(build([1, 2, 2, None, 3, None, 3])))      # Expected: False

    print(isSymmetric(build([1])))                              # Expected: True


'''
Pattern
Bottom-Up recursion comparing MIRRORED pairs of nodes.
A tree is symmetric iff its left and right subtrees are mirror images. We recurse on
pairs (a, b): the outer children must match (a.left with b.right) and the inner
children must match (a.right with b.left). Each pair resolves base cases then ANDs
the verdicts from its two child-pairs, so information flows UP.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  each node is examined once as part of exactly one mirrored pair
| Space  | O(h)  |  recursion stack, h = height (O(n) worst case for a skewed tree)

Better Possible?
No. Confirming symmetry requires inspecting every node, so O(n) time is optimal.
An iterative BFS/queue variant keeps the same O(n) time and O(h) space bounds.
'''
