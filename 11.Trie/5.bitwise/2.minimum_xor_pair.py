'''
2. Minimum XOR Value of Any Two Elements (Medium)
Problem Statement

Given an integer array nums (length >= 2), return the minimum value of
nums[i] XOR nums[j] over all pairs i != j.

Example
Input:
nums = [3,10,5,25,2,8]
Output:
1
Explanation:
2 XOR 3 = 1, which is the smallest XOR among all pairs.

Input:
nums = [1,2,3,4]
Output:
1

Input:
nums = [0,4]
Output:
4
'''


class TrieNode:
    def __init__(self):
        self.children = {}     # bit (0/1) -> TrieNode


HIGH = 31


def minimumXor(nums):
    root = TrieNode()

    def insert(num):
        node = root
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            node = node.children.setdefault(bit, TrieNode())

    def min_xor(num):
        # greedily follow the SAME bit to keep high bits 0; fall back when absent
        node = root
        x = 0
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            if bit in node.children:
                node = node.children[bit]      # same bit -> contributes 0
            else:
                x |= (1 << i)                  # forced to differ at this bit
                node = node.children[1 - bit]
        return x

    best = float("inf")
    # insert first element, then for each later element query the trie of earlier ones
    insert(nums[0])
    for k in range(1, len(nums)):
        best = min(best, min_xor(nums[k]))
        insert(nums[k])
    return best


if __name__ == "__main__":
    print(minimumXor([3, 10, 5, 25, 2, 8]))   # Expected: 1
    print(minimumXor([1, 2, 3, 4]))           # Expected: 1
    print(minimumXor([0, 4]))                 # Expected: 4


'''
Pattern
✅ Bitwise Trie + greedy "same bit" walk (alternative: sort + check adjacent pairs)

Technique & why
To MINIMIZE XOR we want matching high bits, so at each level we greedily descend to
the SAME bit as the query when it exists (that bit contributes 0). Insert elements one
at a time and query the trie of previously inserted numbers, guaranteeing i != j.
Insight: the minimum-XOR pair is always two values that are adjacent when sorted, so a
sort + single adjacent scan also solves it in O(n log n) with O(1) extra space.

| Metric | Value     |
| ------ | --------- |
| Time   | O(n * B)   | (B = bit width)
| Space  | O(n * B)   |

Better Possible?
✅ Yes for space/simplicity: sort the array and take the min XOR over adjacent pairs,
which is O(n log n) time and O(1) extra space and avoids building a trie.
'''
