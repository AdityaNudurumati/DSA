'''
1. Maximum XOR With an Element From Array (Hard)
Problem Statement

You are given an array nums and a list of queries where queries[i] = [x_i, m_i].
The answer to the i-th query is the maximum bitwise XOR of x_i with any element of
nums that does NOT exceed m_i (i.e. nums[j] <= m_i). If no such element exists, the
answer is -1. Return an array of answers, one per query in the ORIGINAL query order.

Example
Input:
nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output:
[3,3,7]
Explanation:
[3,1] -> only {0,1} usable, 3^1=2, 3^0=3 -> 3
[1,3] -> {0,1,2,3} usable, 1^2=3 -> 3
[5,6] -> {0,1,2,3,4} usable, 5^2=7 -> 7

Input:
nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output:
[15,-1,5]
'''


class TrieNode:
    def __init__(self):
        self.children = {}     # bit (0/1) -> TrieNode


HIGH = 29  # values up to ~10^9 fit in 30 bits


def maximizeXor(nums, queries):
    root = TrieNode()

    def insert(num):
        node = root
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            node = node.children.setdefault(bit, TrieNode())

    def max_xor(num):
        # trie assumed non-empty; greedily pick opposite bit
        node = root
        x = 0
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit
            if want in node.children:
                x |= (1 << i)
                node = node.children[want]
            else:
                node = node.children[bit]
        return x

    nums = sorted(nums)
    # attach original index so we can restore answer order after sorting queries
    ordered = sorted(range(len(queries)), key=lambda k: queries[k][1])

    ans = [0] * len(queries)
    j = 0  # pointer into sorted nums: everything < j is already inserted
    for qi in ordered:
        x, m = queries[qi]
        # offline: insert all nums <= m before answering this query
        while j < len(nums) and nums[j] <= m:
            insert(nums[j])
            j += 1
        ans[qi] = max_xor(x) if j > 0 else -1
    return ans


if __name__ == "__main__":
    print(maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))          # Expected: [3, 3, 7]
    print(maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]))      # Expected: [15, -1, 5]


'''
Pattern
✅ Bitwise Trie + offline query processing (sort nums and queries by the m bound)

Technique & why
Sort the queries by their value-limit m and sort nums. Sweep nums with a pointer,
inserting each value <= current m into a binary trie exactly once. Because m is
non-decreasing across processed queries, every insert is permanent and never undone.
A standard max-XOR greedy walk (prefer the opposite bit at each level) then answers
each query against only the eligible elements. Original order is restored via the
saved query indices; an empty trie yields -1.

| Metric | Value                  |
| ------ | ---------------------- |
| Time   | O((n + q)*B + q log q)  | (B = bit width, q = #queries)
| Space  | O(n * B)               |

Better Possible?
❌ Not asymptotically. Offline + trie is the standard optimal approach; a persistent
trie could answer online but adds complexity without beating this for the batch case.
'''
