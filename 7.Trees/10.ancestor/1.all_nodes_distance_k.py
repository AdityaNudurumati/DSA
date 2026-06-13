"""
863. All Nodes Distance K in Binary Tree (Medium)

Problem Statement:
Given the root of a binary tree, a target node, and an integer k, return a list
of the values of all nodes that are at distance k from the target node. The answer
can be returned in any order.

Distance is the number of edges on the shortest path between two nodes. A node's
neighbours are its left child, right child, and parent.

Example:
    Input:  root = [3,5,1,6,2,0,8,None,None,7,4], target = node(5), k = 2
    Output: [1, 4, 7]   (nodes 7,4,1 are exactly 2 edges from 5; sorted for display)
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
    n = len(values)
    while q and i < n:
        node = q.popleft()
        if i < n and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < n and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


def level_order(root):
    """Flatten to a level-order list of values (None for missing) for verification."""
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


def find(root, target_val):
    """Locate the TreeNode whose val == target_val (assumes unique vals)."""
    if not root:
        return None
    q = deque([root])
    while q:
        node = q.popleft()
        if node.val == target_val:
            return node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return None


def distance_k(root, target, k):
    # 1) one DFS to map each node -> its parent, turning the tree into a graph.
    parent = {}

    def dfs(node, par):
        if not node:
            return
        parent[node] = par
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    # 2) BFS outward from target over {left, right, parent}; level k holds the answer.
    visited = {target}
    q = deque([target])
    dist = 0
    while q and dist < k:
        for _ in range(len(q)):
            node = q.popleft()
            for nxt in (node.left, node.right, parent[node]):
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        dist += 1

    return [node.val for node in q]


if __name__ == "__main__":
    root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target = find(root, 5)
    print(sorted(distance_k(root, target, 2)))   # Expected: [1, 4, 7]

    # Edge: k = 0 returns just the target itself.
    print(sorted(distance_k(root, target, 0)))   # Expected: [5]

    # Edge: k larger than tree radius -> no nodes.
    print(sorted(distance_k(root, find(root, 6), 10)))  # Expected: []


"""
Pattern: Ancestor / Descendant — parent mapping + BFS as graph.

Technique & why:
A binary tree only has downward pointers, so "distance" naturally measures
descendants. To also reach ancestors/siblings we first DFS to record each node's
parent, converting the tree into an undirected graph (each node has up to 3
neighbours: left, right, parent). A plain BFS from the target then expands one
ring per level; everything still in the queue after k levels is exactly distance k.

| Metric | Value |
| Time   | O(n)  — one DFS to map parents + one BFS over n nodes |
| Space  | O(n)  — parent map, visited set, and BFS queue |

Better Possible?
No. Every node may need to be visited to build the parent map and to discover the
answer set, so O(n) time and O(n) space are optimal for a single query.
"""
