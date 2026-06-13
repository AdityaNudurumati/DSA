'''
2. Binary Tree Cameras (Hard)
Problem Statement

You are given the root of a binary tree. We install cameras on tree nodes where each
camera at a node can monitor its PARENT, ITSELF, and its immediate CHILDREN.

Return the MINIMUM number of cameras needed to monitor all nodes of the tree.

Example
Input:
root = [0,0,None,0,0]
        0
       /
      0
     / \
    0   0
Output:
1
Explanation:
One camera placed on the middle node covers all four nodes.

Input:
root = [0,0,None,0,None,0,None,None,0]
        0
       /
      0
     /
    0
     \
      0
       \
        0
Output:
2
Explanation:
At least two cameras are needed to monitor this 5-node skewed path.
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node, LeetCode style) -> root
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):                 # left child
            if values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
        if i < len(values):                 # right child
            if values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
    return root


def level_order(root):
    # flatten to a plain list of values, skipping None placeholders
    out = []
    q = deque([root]) if root else deque()
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


def minCameraCover(root):
    # Greedy state DP, post-order. Each node reports one of three states UP:
    #   0 = NOT covered  (needs the parent to put a camera)
    #   1 = covered, no camera here
    #   2 = has a camera here (covers parent too)
    # Strategy: place a camera as LATE as possible (closest to root), i.e. only when
    # a child is uncovered. This is provably optimal for the cover-parent rule.
    cameras = 0

    def dfs(node):
        nonlocal cameras
        if not node:
            return 1                         # null treated as already covered
        l = dfs(node.left)
        r = dfs(node.right)
        if l == 0 or r == 0:                 # a child is uncovered -> must put camera
            cameras += 1
            return 2
        if l == 2 or r == 2:                 # a child has a camera -> we are covered
            return 1
        return 0                             # children covered but none watches us

    # if the root itself ends uncovered, it needs its own camera
    if dfs(root) == 0:
        cameras += 1
    return cameras


if __name__ == "__main__":
    root1 = build([0, 0, None, 0, 0])
    print(level_order(root1))      # Expected: [0, 0, 0, 0]
    print(minCameraCover(root1))   # Expected: 1

    root2 = build([0, 0, None, 0, None, 0, None, None, 0])
    print(level_order(root2))      # Expected: [0, 0, 0, 0, 0]
    print(minCameraCover(root2))   # Expected: 2


'''
Pattern
Tree DP — greedy state DP, post-order three-state propagation.

Technique & why
The naive include/exclude tuple isn't enough because a camera covers THREE levels
(parent, self, children), coupling a node to its grandchildren. We encode each
subtree's interface to its parent as one of three states: NOT-covered(0),
covered-no-camera(1), has-camera(2). Greedy rule: install a camera only when a child
reports 0 (otherwise it could never be covered), and push coverage upward. Placing
cameras as high as possible (delaying until forced by an uncovered child) is optimal
because a camera on a leaf wastes its parent-covering ability. One post-order pass,
O(1) work per node.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(h)  |   (recursion stack, h = tree height)

Better Possible?
No. Each node must be examined, giving an O(n) lower bound; the greedy single pass
already matches it. Space is the unavoidable recursion depth O(h).
'''
