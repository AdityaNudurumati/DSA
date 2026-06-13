"""
4. Boundary Traversal of Binary Tree (Medium)

Problem Statement:
Given the root of a binary tree, return its boundary in ANTI-CLOCKWISE order
starting from the root. The boundary is, in order:
  1. the root,
  2. the left boundary (top -> down, EXCLUDING leaves),
  3. all leaves (left -> right),
  4. the right boundary (down -> up, EXCLUDING leaves) i.e. reversed.
Each node appears at most once.

Example:
    Input:  root = [1,2,3,4,5,6,7]
    Output: [1,2,4,5,6,7,3]
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


def _is_leaf(node):
    return node.left is None and node.right is None


def boundary_traversal(root):
    if not root:
        return []
    result = []
    # Root is always part of the boundary (and not treated as a leaf here).
    if not _is_leaf(root):
        result.append(root.val)

    # 1. Left boundary (top-down), excluding leaves. Prefer left child, else right.
    node = root.left
    while node:
        if not _is_leaf(node):
            result.append(node.val)
        node = node.left if node.left else node.right

    # 2. Leaves, left -> right (full DFS so we catch interior leaves too).
    def add_leaves(n):
        if not n:
            return
        if _is_leaf(n):
            result.append(n.val)
            return
        add_leaves(n.left)
        add_leaves(n.right)
    add_leaves(root)

    # 3. Right boundary (top-down) excluding leaves, collected then reversed.
    stack = []
    node = root.right
    while node:
        if not _is_leaf(node):
            stack.append(node.val)
        node = node.right if node.right else node.left
    result.extend(reversed(stack))

    return result


if __name__ == "__main__":
    # Build tree [1,2,3,4,5,6,7]
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4   5 6   7
    # root=1 | left boundary (no non-leaf)=[2] | leaves=[4,5,6,7] | right rev=[3]
    root = build([1, 2, 3, 4, 5, 6, 7])
    print(boundary_traversal(root))  # Expected: [1, 2, 4, 5, 6, 7, 3]


"""
Pattern: Tree Views — Boundary as three disjoint linear walks.
Technique: split the outline into root + left edge + leaves + reversed right edge.
Walk the left edge top-down skipping leaves (following left, falling back to right
when no left child). Collect all leaves via a left-to-right DFS. Walk the right
edge top-down skipping leaves into a stack, then append it reversed for the
bottom-up half. Excluding leaves from the edge walks prevents duplicates with the
leaf pass; the single root entry is the anti-clockwise start.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |  (recursion / stack for leaves + right edge buffer)

Better Possible?
No on time — every node may sit on the boundary so O(n) is required. The leaf DFS
recursion can be made iterative to bound auxiliary space at O(h) plus the edge
buffer, but asymptotics are unchanged.
"""
