'''
1. Single Number (Easy)
Problem Statement

Given a non-empty array where every element appears twice except one, find that
single one. Must be O(n) time and O(1) extra space.

Example
Input:
nums = [4,1,2,1,2]

Output:
4
'''

def singleNumber(nums):

    result = 0
    for x in nums:
        result ^= x         # pairs cancel (a ^ a = 0); the loner survives

    return result


if __name__ == "__main__":
    print(singleNumber([2, 2, 1]))         # Expected: 1
    print(singleNumber([4, 1, 2, 1, 2]))   # Expected: 4

'''
Pattern
✅ XOR cancellation

Key Observation
XOR is associative/commutative and a ^ a = 0, so every duplicated value cancels,
leaving only the unique number.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
