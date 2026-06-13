'''
257. Binary Tree Paths (Easy)
Problem Statement

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children. Each path is represented as a string of node
values joined by "->".

Example:
Input:  root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Explanation:
        1
       / \
      2   3
       \
        5
Root-to-leaf paths: 1->2->5 and 1->3.
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
    # Standard BFS listing (used by other helpers/verification).
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


def binaryTreePaths(root):
    # TOP-DOWN: carry the path-so-far DOWN into the recursion as accumulated state.
    paths = []

    def dfs(node, acc):
        if not node:
            return
        acc = acc + [str(node.val)]          # extend state with current node
        if not node.left and not node.right:  # leaf -> finalize one path
            paths.append("->".join(acc))
            return
        dfs(node.left, acc)                   # pass state down to children
        dfs(node.right, acc)

    dfs(root, [])
    return paths


if __name__ == "__main__":
    root = build([1, 2, 3, None, 5])
    print(binaryTreePaths(root))  # Expected: ['1->2->5', '1->3']

    print(binaryTreePaths(build([1])))  # Expected: ['1']

    print(binaryTreePaths(build([])))   # Expected: []


'''
Pattern
Top-Down recursion (DFS carrying accumulated state).
We push the running list of values DOWN the tree; when we hit a leaf we have the
full root-to-leaf path ready to emit. No information needs to come back up, so the
work happens on the way down. This is the classic dfs(node, acc) template.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  visit each node once; joining paths is O(total path length) = O(n) for a balanced tree, O(n^2) worst case (degenerate/skewed tree)
| Space  | O(h)  |  recursion stack + path buffer, h = tree height (O(n) worst case)

Better Possible?
No. Every node must be visited to discover the leaves, so O(n) time is optimal.
The output itself can be O(n) to O(n^2) in size, which lower-bounds the work.
'''
