'''
1. Jewels and Stones (Easy)
Problem Statement

You are given strings jewels and stones. Each character in stones is a type of
stone you have. Each character in jewels is a type that counts as a jewel.
Return how many of your stones are also jewels. Letters are case-sensitive.

Example
Input:
jewels = "aA", stones = "aAAbbbb"

Output:
3
'''

def numJewelsInStones(jewels, stones):

    # put jewel types in a set for O(1) membership checks
    jewel_set = set(jewels)

    # count stones whose type is a jewel
    return sum(1 for s in stones if s in jewel_set)


if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))   # Expected: 3

'''
Pattern
✅ Set Based (membership lookup)

Key Observation
A set of jewel characters turns each "is this stone a jewel?" test into O(1),
so one scan over stones gives the count.

| Metric | Value |
| ------ | ----- |
| Time   | O(j + s) |
| Space  | O(j)  |

Better Possible?
O(j + s) is optimal — every stone must be inspected. j, s = lengths of jewels
and stones.
'''
