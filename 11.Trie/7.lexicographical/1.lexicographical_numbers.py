"""
386. Lexicographical Numbers (Medium)

Problem Statement:
Given an integer n, return all the integers in the range [1, n] sorted in
lexicographical (dictionary) order. You must write an algorithm that runs in
O(n) time and uses O(1) extra space (besides the output list).

Example:
    Input:  n = 13
    Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

    Input:  n = 2
    Output: [1, 2]
"""


class TrieNode:
    """A node in the conceptual denary (10-ary) trie over digits 0..9.

    We never build the trie explicitly: the integers 1..n already form a
    10-ary trie where the children of value v are 10*v..10*v+9. A pre-order
    DFS that visits children in ascending digit order yields lexicographic
    order. This node type documents that mental model.
    """

    def __init__(self, value):
        self.value = value          # integer represented by the path to here
        self.children = {}          # digit -> TrieNode (built lazily if ever)


def lexical_order(n):
    # Iterative pre-order walk of the denary trie rooted at digits 1..9.
    # 'cur' is the current number; we go as deep as possible (append a 0),
    # otherwise move to the next sibling, climbing when we overflow n or hit 9.
    res = []
    cur = 1
    for _ in range(n):
        res.append(cur)
        if cur * 10 <= n:
            cur *= 10                       # descend to leftmost child
        else:
            while cur % 10 == 9 or cur + 1 > n:
                cur //= 10                  # climb until a valid sibling exists
            cur += 1                        # move to next sibling
    return res


if __name__ == "__main__":
    print(lexical_order(13))  # Expected: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lexical_order(2))   # Expected: [1, 2]

"""
Pattern: Lexicographical Trie (sorted pre-order DFS of a denary trie).
Technique: the numbers 1..n form an implicit 10-ary trie whose children of v are
10v..10v+9. Visiting children in ascending order during a pre-order traversal emits
values in dictionary order. We simulate the DFS with a single cursor: descend by
multiplying by 10, and when we cannot descend we advance to the next sibling,
climbing out of full/overflowed branches first.
Why: dictionary order is exactly the order a left-to-right pre-order walk produces;
no sorting of strings is needed, giving linear time and constant extra space.

| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Every number in [1, n] must appear in the output, so O(n) time is a lower bound;
the cursor walk already uses only O(1) auxiliary space beyond the result.
"""
