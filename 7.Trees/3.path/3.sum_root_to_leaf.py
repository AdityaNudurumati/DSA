"""
129. Sum Root to Leaf Numbers (Medium)

Problem Statement:
You are given the root of a binary tree containing digits from 0 to 9. Each
root-to-leaf path represents a number (e.g. 1 -> 2 -> 3 is the number 123).
Return the total sum of all root-to-leaf numbers. A leaf is a node with no
children. The answer fits in a 32-bit integer.

Example:
    Input:  root = [1,2,3]
    Output: 25          (12 + 13)

    Input:  root = [4,9,0,5,1]
    Output: 1026        (495 + 491 + 40)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node, LeetCode style) -> root."""
    if not values or values[0] is None:
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


def sum_numbers(root):
    # Top-down: build the running number by `cur*10 + digit`; add it at leaves.
    def dfs(node, cur):
        if not node:
            return 0
        cur = cur * 10 + node.val
        if not node.left and not node.right:   # leaf -> finished number
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)

    return dfs(root, 0)


if __name__ == "__main__":
    print(sum_numbers(build([1, 2, 3])))          # Expected: 25
    print(sum_numbers(build([4, 9, 0, 5, 1])))    # Expected: 1026


"""
Pattern: PATH-BASED (Root -> Leaf accumulation)
Technique: top-down DFS carrying the partially-formed number downward. Each
step shifts the accumulator one decimal place and appends the current digit;
completed numbers are summed at leaves. Passing state DOWN avoids any global
buffer.

| Metric | Value |
| Time   | O(n)  — one visit per node |
| Space  | O(h)  — recursion stack |

Better Possible?
O(n) time is optimal (every digit must be read). Space is bounded by tree
height; an explicit-stack iterative version achieves the same O(h).
"""
