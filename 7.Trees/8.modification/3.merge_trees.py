'''
3. Merge Two Binary Trees (Easy)
Problem Statement

You are given the roots of two binary trees root1 and root2. Imagine overlaying
one tree on top of the other. Merge them into a new tree such that:
- if two nodes overlap, the merged node value is the SUM of the two values;
- otherwise, the non-null node is used as the merged node.

Return the root of the merged tree (you may reuse root1's nodes).

Input:
root1 = [1,3,2,5]
root2 = [2,1,3,None,4,None,7]

Output:
[3,4,5,5,4,None,7]   (level-order of the merged tree)
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


def mergeTrees(root1, root2):
    # if one side is missing, the other subtree IS the merged subtree
    if not root1:
        return root2
    if not root2:
        return root1
    # both present: sum values, then merge children pairwise
    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    return root1


if __name__ == "__main__":
    t1 = build([1, 3, 2, 5])
    t2 = build([2, 1, 3, None, 4, None, 7])
    print(level_order(mergeTrees(t1, t2)))  # Expected: [3, 4, 5, 5, 4, None, 7]


'''
Pattern
Tree Modification — simultaneous two-tree recursion (overlay).
Walk both trees in lockstep. The two base cases collapse to "return whichever
node exists" so a missing node contributes nothing; when both exist, add the
values and recurse on the matching child pairs. Reusing root1's nodes makes it
an in-place merge.

| Metric | Value           |
| ------ | --------------- |
| Time   | O(min(n1, n2))  |   (recursion stops at any pair where one side is None)
| Space  | O(min(h1, h2))  |   (recursion stack)

Better Possible?
No. We must look at every overlapping node at least once, and recursion stops as
soon as one tree runs out, so O(min(n1, n2)) is optimal. An iterative stack/BFS
version trades the recursion stack for an explicit one with the same bounds.
'''
