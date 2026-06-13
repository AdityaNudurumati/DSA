"""
145. Binary Tree Postorder Traversal (Easy)

Problem Statement
-----------------
Given the root of a binary tree, return the postorder traversal of its nodes'
values. Solve it iteratively (without recursion) using an explicit stack.

Postorder = Left -> Right -> Node.

Example
-------
Input:  root = [1, None, 2, 3]
Output: [3, 2, 1]

Input:  root = [1, 2, 3, 4, 5]
Output: [4, 5, 2, 3, 1]
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node, LeetCode style) -> root."""
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        node = q[0]
        if not hasattr(node, "_l"):
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
            node._l = True
        else:
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
            q.popleft()
    return root


def postorder(root):
    """Recursive postorder, used only to cross-check the iterative result."""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def postorder_iterative(root):
    # Trick: a modified preorder (Node -> Right -> Left) reversed gives
    # postorder (Left -> Right -> Node). Push left BEFORE right so right pops
    # first, then reverse the collected order at the end.
    if not root:
        return []
    stack, out = [root], []
    while stack:
        node = stack.pop()
        out.append(node.val)          # collect Node first (root...->...leaf)
        if node.left:
            stack.append(node.left)   # left pushed first -> popped later
        if node.right:
            stack.append(node.right)  # right pushed last -> popped sooner
    return out[::-1]                  # reverse Node->Right->Left into Left->Right->Node


if __name__ == "__main__":
    t1 = build([1, None, 2, 3])
    print(postorder_iterative(t1))         # Expected: [3, 2, 1]

    t2 = build([1, 2, 3, 4, 5])
    print(postorder_iterative(t2))         # Expected: [4, 5, 2, 3, 1]


"""
Pattern
-------
Iterative Postorder via the "reverse of modified preorder" stack trick. A normal
iterative preorder visits Node, Left, Right. If we instead push left before right
we get Node, Right, Left; reversing that sequence yields Left, Right, Node, which
is exactly postorder. One stack, one pass, then a single reverse.

| Metric        | Value |
| Time          | O(n)  |
| Space         | O(n)  |   (stack + output; O(h) for the stack alone)

Better Possible?
Time is optimal O(n). Space for the stack is O(h); the extra O(n) comes from the
output list which is unavoidable since we must return all values. A two-stack or
single-stack-with-lastVisited variant uses the same asymptotics but avoids the
final reverse; Morris postorder can reach O(1) auxiliary space at the cost of
more intricate pointer rewiring.
"""
