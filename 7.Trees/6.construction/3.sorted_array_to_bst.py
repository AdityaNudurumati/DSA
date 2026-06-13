'''
3. Convert Sorted Array to Binary Search Tree (Easy)
Problem Statement

Given an integer array nums sorted in ascending order, convert it to a
height-balanced binary search tree.

A height-balanced BST is one where the depth of the two subtrees of every node
never differs by more than one.

Input:
nums = [-10,-3,0,5,9]

Output (inorder):
[-10,-3,0,5,9]    (a BST's inorder is the sorted array)

The tree is height-balanced (height <= 3 for 5 nodes). One valid result:
      0
     / \
   -3   9
   /    /
 -10   5
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # level-order list (None = missing node) -> root
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
    return root


def inorder(root):
    # left -> root -> right yields the BST values in sorted order
    out = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)

    dfs(root)
    return out


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def sortedArrayToBST(nums):
    # Picking the MIDDLE element as the root guarantees the two halves differ in
    # size by at most one -> the resulting tree is height-balanced. Recurse on
    # the left and right halves to build the subtrees.
    def helper(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        root = TreeNode(nums[mid])
        root.left = helper(lo, mid - 1)
        root.right = helper(mid + 1, hi)
        return root

    return helper(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    root = sortedArrayToBST(nums)
    print(inorder(root))            # Expected: [-10, -3, 0, 5, 9]

    h = height(root)
    print(h <= 3)                   # Expected: True  (balanced, height <= 3)


'''
Pattern
Tree Construction — Sorted Array -> Balanced BST via Divide & Conquer.
The middle element becomes the subtree root so each side holds (near) equal counts,
keeping height ~log2(n). Recursing on [lo, mid-1] and [mid+1, hi] mirrors a binary
search and never builds a skewed chain.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(log n) |  (recursion stack; O(n) for the tree itself)

Better Possible?
No. Every element must become a node, so O(n) time is optimal. Choosing the middle
as root is what guarantees the minimum-possible height (ceil(log2(n+1))).
'''
