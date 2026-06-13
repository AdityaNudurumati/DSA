"""
1483. Kth Ancestor of a Tree Node (Hard)

Problem Statement:
You are given a tree with n nodes numbered 0 .. n-1 in the form of a parent array
where parent[i] is the parent of node i, and parent[0] == -1 because node 0 is the
root. Implement TreeAncestor(n, parent) and a method getKthAncestor(node, k) that
returns the k-th ancestor of the given node, or -1 if it does not exist.

The k-th ancestor of a node is the k-th node on the path from that node up to the root.

Example:
    Input:
        TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
        getKthAncestor(3, 1) -> 1
        getKthAncestor(5, 2) -> 0
        getKthAncestor(6, 3) -> -1
    Output: [1, 0, -1]

(No TreeNode here: the tree is supplied as a flat parent array, which is exactly
what binary lifting wants — but we still keep the standard helpers below so the
file matches the pattern's self-contained shape.)
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    """Level-order list (None = missing node) -> root. (Helper kept for consistency.)"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i, n = 1, len(values)
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
    """Flatten to a level-order list of values (None for missing)."""
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


class TreeAncestor:
    """Binary lifting: up[j][v] = the (2**j)-th ancestor of node v."""

    def __init__(self, n, parent):
        # LOG = smallest power of two >= n, so any k < n is expressible in binary.
        self.LOG = max(1, (n - 1).bit_length()) if n > 1 else 1
        # up[0] is the immediate parent; -1 marks "no ancestor".
        self.up = [parent[:]]
        for j in range(1, self.LOG):
            prev = self.up[j - 1]
            cur = [-1] * n
            for v in range(n):
                mid = prev[v]              # 2**(j-1)-th ancestor
                if mid != -1:
                    cur[v] = prev[mid]     # jump another 2**(j-1) steps
            self.up.append(cur)

    def getKthAncestor(self, node, k):
        # Walk up by powers of two corresponding to the set bits of k.
        for j in range(self.LOG):
            if node == -1:
                break
            if (k >> j) & 1:
                node = self.up[j][node]
        return node


if __name__ == "__main__":
    ta = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(ta.getKthAncestor(3, 1))   # Expected: 1
    print(ta.getKthAncestor(5, 2))   # Expected: 0
    print(ta.getKthAncestor(6, 3))   # Expected: -1

    # Extra checks:
    print(ta.getKthAncestor(6, 0))   # Expected: 6   (0th ancestor is itself)
    print(ta.getKthAncestor(0, 1))   # Expected: -1  (root has no parent)


"""
Pattern: Ancestor / Descendant — binary lifting (sparse ancestor table).

Technique & why:
Naively walking up k parents costs O(k) per query, which is slow when there are
many queries on a tall tree. Binary lifting precomputes, for every node, its
2^0, 2^1, 2^2, ... ancestors. Any k is a sum of distinct powers of two (its binary
representation), so each query jumps along the set bits of k and reaches the
k-th ancestor in O(log k) hops. up[j][v] = up[j-1][ up[j-1][v] ] composes two
half-jumps, which is the doubling trick.

| Metric          | Value |
| Build time      | O(n log n) — fill a LOG x n table |
| Query time      | O(log k) per getKthAncestor call |
| Space           | O(n log n) — the lifting table |

Better Possible?
For the general "many queries, arbitrary k" setting, O(log k) per query is the
standard optimum and binary lifting is the canonical answer. With heavier
preprocessing (Euler tour + level ancestor / ladder decomposition) one can reach
O(1) per query, but that is far more complex and rarely needed in interviews.
"""
