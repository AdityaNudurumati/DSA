'''
315. Count of Smaller Numbers After Self (Hard)
Problem Statement

Given an integer array nums, return an integer array counts where counts[i] is
the number of elements to the right of nums[i] that are strictly smaller than it.

Example
Input:
  nums = [5, 2, 6, 1]
Output:
  [2, 1, 1, 0]
Explanation:
  Right of 5 -> {2, 1}  -> 2 smaller
  Right of 2 -> {1}     -> 1 smaller
  Right of 6 -> {1}     -> 1 smaller
  Right of 1 -> {}      -> 0 smaller

Input:
  nums = [-1, -1]
Output:
  [0, 0]
'''

from collections import deque


# ---- Minimal TreeNode + helpers (required by repo convention) ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def build(values):
    # Level-order list (None = missing node, LeetCode style) -> root.
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q, i = deque([root]), 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return root


def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out


# ---- Solution: Fenwick / BIT over compressed ranks ----
def countSmaller(nums):
    n = len(nums)
    if n == 0:
        return []

    # Coordinate-compress values to ranks 1..m (1-indexed for the BIT).
    sorted_unique = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    m = len(sorted_unique)

    bit = [0] * (m + 1)

    def add(i):
        while i <= m:
            bit[i] += 1
            i += i & (-i)

    def query(i):                      # how many inserted values have rank <= i
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    res = [0] * n
    # Walk right-to-left: BIT holds counts of values already seen on the right.
    # Smaller-than-current = values with rank <= rank(current) - 1.
    for idx in range(n - 1, -1, -1):
        r = rank[nums[idx]]
        res[idx] = query(r - 1)
        add(r)
    return res


if __name__ == "__main__":
    print(countSmaller([5, 2, 6, 1]))   # Expected: [2, 1, 1, 0]
    print(countSmaller([-1, -1]))       # Expected: [0, 0]

    # Helpers demo:
    print(level_order(build([5, 2, 6, 1])))  # Expected: [5, 2, 6, 1]

'''
Pattern
Fenwick Tree / BIT with coordinate compression (rank counting)

Technique & why
"Count smaller elements to the right" is an order-statistic query. Scanning from
right to left, the BIT maintains how many already-seen (i.e. to-the-right) values
fall in each rank bucket. For the current element we ask query(rank - 1): the
number of seen values strictly smaller. Coordinate compression maps arbitrary /
negative values into a dense 1..m index range so the BIT stays O(m). Each step is
one O(log m) query + one O(log m) update.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
O(n log n) is the lower bound for this comparison-based counting problem (it is
equivalent to counting inversions). A merge-sort-with-index approach or a
balanced BST hits the same bound; none beats it asymptotically, so this is
optimal.
'''
