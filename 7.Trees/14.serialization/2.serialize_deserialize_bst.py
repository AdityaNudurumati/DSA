'''
2. Serialize and Deserialize BST (Medium)
Problem Statement

Serialization is converting a data structure into a string for storage or
transmission; deserialization rebuilds it. Design a codec for a Binary Search
Tree (BST) and encode the tree as compactly as you can.

Because the input is a BST (left < root < right), we can store ONLY the values
in preorder, with NO null markers, and still rebuild the exact tree: the BST
ordering tells us where each subtree begins and ends.

Input:
root = [2,1,3]   # LeetCode level-order, a valid BST

Output:
[2,1,3]          # level-order of the round-tripped BST

Explanation:
serialize(root) -> "2,1,3"; deserialize uses value bounds to place 1 in the
left subtree and 3 in the right subtree, rebuilding the same BST.
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
    while out and out[-1] is None:
        out.pop()
    return out


class Codec:
    # Preorder WITHOUT null markers; BST property reconstructs the shape.
    def serialize(self, root):
        out = []

        def dfs(n):
            if not n:
                return
            out.append(str(n.val))   # preorder: root before children
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data):
        if not data:
            return None
        vals = [int(x) for x in data.split(",")]
        idx = [0]                    # mutable cursor into the preorder list

        def make(lo, hi):
            # consume next value only if it fits the current (lo, hi) BST window
            if idx[0] == len(vals):
                return None
            v = vals[idx[0]]
            if v < lo or v > hi:
                return None
            idx[0] += 1
            n = TreeNode(v)
            n.left = make(lo, v)     # left subtree: values must be < v
            n.right = make(v, hi)    # right subtree: values must be > v
            return n

        return make(float("-inf"), float("inf"))


if __name__ == "__main__":
    codec = Codec()

    root = build([2, 1, 3])
    encoded = codec.serialize(root)
    decoded = codec.deserialize(encoded)
    print(level_order(decoded))   # Expected: [2, 1, 3]

    # Edge: empty BST round-trips to empty
    print(level_order(codec.deserialize(codec.serialize(build([])))))  # Expected: []


'''
Pattern
Preorder serialization exploiting the BST invariant (no null markers).

Why: in a BST, preorder = [root, all-values < root, all-values > root]. During
rebuild we carry a (lo, hi) bound for the slot we are filling and only take the
next value when it lies inside that window; otherwise the subtree is empty.
This lets us drop the explicit '#' sentinels that a general binary tree needs,
giving a strictly smaller encoding while staying unambiguous.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  each value is pushed once and consumed once
| Space  | O(n)  |  value list + O(h) recursion stack

Better Possible?
No (asymptotically). O(n) is optimal since every value must be emitted and
read. Versus the general-tree codec, this is a constant-factor win: it stores
n numbers instead of n values plus up to n+1 null markers. Bit-packing could
shrink the string further but not the O(n) order.
'''
