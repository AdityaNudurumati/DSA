'''
1. Maximum XOR of Two Numbers in an Array (Medium)
Problem Statement

Given an integer array nums, return the maximum value of nums[i] XOR nums[j].
(Also known as "Maximum XOR Pair".)

Example
Input:
nums = [3,10,5,25,2,8]

Output:
28
Explanation:
5 XOR 25 = 28.
'''

def findMaximumXOR(nums):

    HIGH = max(nums).bit_length() - 1 if max(nums) > 0 else 0
    root = {}

    # insert every number into a bitwise trie (most significant bit first)
    for num in nums:
        node = root
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            node = node.setdefault(bit, {})

    best = 0
    # for each number, greedily walk toward the OPPOSITE bit to maximize XOR
    for num in nums:
        node = root
        cur = 0
        for i in range(HIGH, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit
            if want in node:
                cur |= (1 << i)
                node = node[want]
            else:
                node = node[bit]
        best = max(best, cur)

    return best


if __name__ == "__main__":
    print(findMaximumXOR([3, 10, 5, 25, 2, 8]))   # Expected: 28
    print(findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))  # Expected: 127

'''
Pattern
✅ Bitwise Trie + greedy bit matching

Key Observation
To maximize XOR for a number, prefer the opposite bit at each level. A binary trie
of the numbers' bits lets each query follow the opposite path greedily.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n * B)   | (B = bit width)
| Space  | O(n * B)   |

Better Possible?
❌ No meaningfully better. (Brute force is O(n²).)
'''
