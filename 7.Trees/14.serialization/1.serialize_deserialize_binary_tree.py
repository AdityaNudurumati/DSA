'''
1. Serialize and Deserialize Binary Tree (Hard)
Problem Statement

Serialization is the process of converting a data structure into a string so it
can be stored or transmitted, and deserialization is rebuilding the original
structure from that string.

Design an algorithm to serialize a binary tree to a single string and to
deserialize that string back into the exact same tree. There is no restriction
on the tree shape or node values (values may be negative).

Input:
root = [1,2,3,None,None,4,5]   # LeetCode level-order

Output:
[1,2,3,None,None,4,5]          # level-order of the round-tripped tree

Explanation:
serialize(root) -> some string; deserialize(string) rebuilds an identical tree,
so its level-order matches the original.
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node) -> root
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        node = q[0]
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        # second child for this node
        try:
            v2 = next(it)
        except StopIteration:
            v2 = None
        if v2 is not None:
            node.right = TreeNode(v2)
            q.append(node.right)
        q.popleft()
    return root


def level_order(root):
    # LeetCode-style level-order list with trailing Nones trimmed
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:   # trim trailing nulls
        out.pop()
    return out


class Codec:
    # Preorder DFS with '#' markers for null children. Handles any value/shape.
    def serialize(self, root):
        out = []

        def dfs(n):
            if not n:
                out.append("#")
                return
            out.append(str(n.val))
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def make():
            v = next(vals)
            if v == "#":
                return None
            n = TreeNode(int(v))
            n.left = make()      # preorder: left subtree consumes next tokens
            n.right = make()
            return n

        return make()


if __name__ == "__main__":
    codec = Codec()

    root = build([1, 2, 3, None, None, 4, 5])
    encoded = codec.serialize(root)
    decoded = codec.deserialize(encoded)
    print(level_order(decoded))   # Expected: [1, 2, 3, None, None, 4, 5]

    # Edge: empty tree round-trips to empty
    print(level_order(codec.deserialize(codec.serialize(build([])))))  # Expected: []


'''
Pattern
Preorder DFS serialization with null markers.

Why: a preorder stream "value, left-subtree, right-subtree" plus an explicit
sentinel ('#') for missing children captures both structure AND values
unambiguously. Deserialization mirrors the same preorder recursion, consuming
tokens left-to-right, so each node knows exactly where its subtrees end. No
inorder companion is needed because the null markers fix the shape.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  serialize + deserialize each touch every node/null once
| Space  | O(n)  |  output string + recursion stack (O(h) stack, O(n) string)

Better Possible?
No (asymptotically). Every node must be written and read at least once, so
O(n) is optimal. BFS (level-order with markers) is an equally valid alternative
with the same complexity; the constant-factor string size can be trimmed but
not the order.
'''
