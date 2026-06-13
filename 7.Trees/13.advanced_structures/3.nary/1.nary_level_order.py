'''
429. N-ary Tree Level Order Traversal (Medium)
Problem Statement

Given an n-ary tree, return the level order traversal of its nodes' values
(i.e. from left to right, level by level).

The n-ary tree input is serialized in level order, where each group of children
is separated by a None value (LeetCode format). For example:
  [1, None, 3, 2, 4, None, 5, 6]
describes a root 1 with children [3, 2, 4]; node 3 has children [5, 6].

Example
Input:
  root = [1, None, 3, 2, 4, None, 5, 6]
Output:
  [[1], [3, 2, 4], [5, 6]]
'''

from collections import deque


# ---- N-ary node + level-order-with-None-separators builder ----
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# Also provide the binary TreeNode + helpers required by repo convention.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Binary level-order builder (None = missing) -> root. Kept for convention.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q, i = deque([root]), 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return root


def level_order(root):
    # Binary level-order values (convention helper).
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


def build_nary(values):
    # LeetCode n-ary format: first val is root, then None, then groups of
    # children each terminated by None when the next parent begins.
    if not values:
        return None
    root = Node(values[0])
    q = deque([root])
    i = 1
    # Skip the leading separator that follows the root.
    if i < len(values) and values[i] is None:
        i += 1
    while i < len(values) and q:
        parent = q.popleft()
        # Consume children until a None separator (or end of list).
        while i < len(values) and values[i] is not None:
            child = Node(values[i])
            parent.children.append(child)
            q.append(child)
            i += 1
        i += 1  # skip the None separator
    return root


# ---- Solution: BFS level by level ----
def levelOrder(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):          # process exactly this level
            node = q.popleft()
            level.append(node.val)
            q.extend(node.children)      # enqueue all children, any arity
        res.append(level)
    return res


if __name__ == "__main__":
    root = build_nary([1, None, 3, 2, 4, None, 5, 6])
    print(levelOrder(root))   # Expected: [[1], [3, 2, 4], [5, 6]]

    # Binary helpers demo (convention):
    print(level_order(build([1, 2, 3])))  # Expected: [1, 2, 3]

'''
Pattern
N-ary Tree BFS (level-order with a children list)

Technique & why
The only difference from a binary level-order traversal is that each node has an
arbitrary-length children list instead of fixed left/right pointers. We snapshot
the current queue size to delimit one level, pop exactly that many nodes into a
level bucket, and enqueue every child via q.extend(node.children). Each node is
enqueued and dequeued once.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (queue width, up to the widest level)

Better Possible?
No. Every node must be visited and emitted, so O(n) time is a hard lower bound;
the output itself is O(n), so O(n) space is also unavoidable. This is optimal.
'''
