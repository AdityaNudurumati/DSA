'''
4. Binary Tree Pruning (Medium)
Problem Statement

Given the root of a binary tree where every node value is 0 or 1, prune the tree
so that every subtree NOT containing a 1 is removed.

A subtree of a node is that node plus all of its descendants. Return the root of
the pruned tree (it may become empty / None).

Input:
root = [1,None,0,0,1]   (level-order, None = missing)

Output:
[1,None,0,None,1]       (level-order of the pruned tree)
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node, LeetCode style) -> root
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            lv = next(it)
        except StopIteration:
            break
        if lv is not None:
            node.left = TreeNode(lv)
            q.append(node.left)
        try:
            rv = next(it)
        except StopIteration:
            break
        if rv is not None:
            node.right = TreeNode(rv)
            q.append(node.right)
    return root


def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def pruneTree(node):
    # post-order: prune children first, then decide on this node.
    if not node:
        return None
    node.left = pruneTree(node.left)
    node.right = pruneTree(node.right)
    # drop this node only if it holds 0 AND both subtrees are now empty
    if node.val == 0 and node.left is None and node.right is None:
        return None
    return node


if __name__ == "__main__":
    root = build([1, None, 0, 0, 1])
    print(level_order(pruneTree(root)))  # Expected: [1, None, 0, None, 1]


'''
Pattern
Tree Modification — bottom-up pruning (post-order).
Decide leaf-up: prune both children first, then this node is removable iff it is
a 0 and (after pruning) has no remaining children. Doing children before the
parent is essential, because pruning a child can turn its parent into a new
prunable leaf (cascading removal of all-zero subtrees).

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack, h = tree height)

Better Possible?
No on time — each node must be inspected once to know whether its subtree holds
a 1, so O(n) is optimal. Space is bounded by tree height; an explicit-stack
iterative post-order would match O(h) without improving the asymptotics.
'''
