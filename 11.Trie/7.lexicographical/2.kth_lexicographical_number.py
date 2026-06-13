"""
440. K-th Smallest in Lexicographical Order (Hard)

Problem Statement:
Given two integers n and k, return the k-th lexicographically smallest integer
in the range [1, n]. The integers are ordered as strings in dictionary order,
e.g. for n = 13 the order is 1,10,11,12,13,2,3,...,9.

Example:
    Input:  n = 13,  k = 2
    Output: 10

    Input:  n = 1,   k = 1
    Output: 1

    Input:  n = 100, k = 10
    Output: 17
"""


class TrieNode:
    """Conceptual node of the denary trie over [1, n].

    The numbers 1..n form a 10-ary trie; the children of prefix p are
    10p..10p+9. We navigate this trie by subtree size: 'count_in_subtree'
    tells how many numbers <= n live under a prefix, letting us skip whole
    branches instead of enumerating them.
    """

    def __init__(self, prefix):
        self.prefix = prefix        # the integer prefix this node represents


def _count_in_subtree(prefix, n):
    # How many integers in [1, n] start with `prefix` (i.e. live in its subtree)?
    # Walk level by level: prefix covers [prefix, prefix+1), [10*prefix, 10*prefix+10), ...
    count = 0
    cur = prefix          # leftmost number on the current level
    nxt = prefix + 1      # first number on the next sibling (level boundary)
    while cur <= n:
        count += min(n + 1, nxt) - cur   # clamp the level's right edge to n
        cur *= 10
        nxt *= 10
    return count


def find_kth_number(n, k):
    # Start at prefix 1 (the smallest 1-digit number), having "used" rank 1.
    cur = 1
    k -= 1                                  # cur itself is the current k-th candidate
    while k > 0:
        steps = _count_in_subtree(cur, n)   # numbers under the cur-prefix subtree
        if steps <= k:
            cur += 1                        # skip this whole subtree, go to next sibling
            k -= steps
        else:
            cur *= 10                       # answer is inside; descend one level
            k -= 1                          # consume cur (the new prefix) itself
    return cur


if __name__ == "__main__":
    print(find_kth_number(13, 2))    # Expected: 10
    print(find_kth_number(1, 1))     # Expected: 1
    print(find_kth_number(100, 10))  # Expected: 17

"""
Pattern: Lexicographical Trie (k-th item via subtree-size navigation).
Technique: model [1, n] as a 10-ary trie where children of prefix p are 10p..10p+9.
Instead of listing numbers, count how many fall under each prefix subtree; if k lies
beyond the current subtree, skip it entirely (advance to the next sibling) and
decrement k by that count, otherwise descend into it. This is the classic "denary
trie" walk guided by subtree cardinalities.
Why: counting a subtree is O(log n) (one term per digit level), and we take at most
O(log n) navigation steps, so we reach the k-th value without materializing the list.

| Metric | Value         |
|--------|---------------|
| Time   | O((log n)^2)  |
| Space  | O(1)          |

Better Possible?
Not meaningfully. The bound is polylogarithmic in n; enumerating to the k-th element
would be O(k) which is far worse for large n. The subtree-count navigation is optimal
for this prefix-ordered problem.
"""
