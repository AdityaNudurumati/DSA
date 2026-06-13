'''
2. Flatten Binary Tree to Linked List (Medium)
Problem Statement

Given the root of a binary tree, flatten it into a "linked list" in place.
- The linked list uses the same TreeNode class, where the right child points
  to the next node and the left child is always None.
- The order of nodes must follow the tree's PREORDER traversal.

Input:
root = [1,2,5,3,4,None,6]   (level-order, None = missing)

Output:
[1,2,3,4,5,6]               (the right-skewed chain of values, root -> right -> ...)
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


def right_chain(root):
    # follow .right pointers, collecting values (verifies the flattened list)
    out = []
    while root:
        out.append(root.val)
        # confirm left links are cleared as required
        out_left = root.left
        assert out_left is None, "left pointer must be None after flatten"
        root = root.right
    return out


def flatten(root):
    # Morris-style rewiring: for each node with a left subtree, splice that
    # subtree between the node and its right subtree (preorder property).
    cur = root
    while cur:
        if cur.left:
            # find rightmost node of the left subtree (preorder predecessor of cur.right)
            prev = cur.left
            while prev.right:
                prev = prev.right
            prev.right = cur.right   # attach old right after left subtree
            cur.right = cur.left     # move left subtree to the right
            cur.left = None          # clear left pointer
        cur = cur.right
    return root


if __name__ == "__main__":
    root = build([1, 2, 5, 3, 4, None, 6])
    flatten(root)
    print(right_chain(root))  # Expected: [1, 2, 3, 4, 5, 6]


'''
Pattern
Tree Modification — in-place preorder rewiring (Morris-flatten).
For each node that has a left subtree, find the rightmost (last preorder) node
of that left subtree, hang the current right subtree off it, then move the whole
left subtree over to the right and null out left. Advancing along .right walks
the tree in exactly preorder while stitching the list together.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |   (each edge visited a constant number of times)
| Space  | O(1)  |   (no recursion, no stack)

Better Possible?
No. Every node must be touched to relink it, so O(n) time is optimal, and the
Morris approach already achieves O(1) extra space (better than the O(h) of the
recursive / explicit-stack solutions).
'''
