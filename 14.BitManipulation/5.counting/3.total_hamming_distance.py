'''
3. Total Hamming Distance (Medium)
Problem Statement

The Hamming distance between two integers is the number of positions at which
the corresponding bits differ.

Given an integer array nums, return the sum of Hamming distances between all
pairs of the integers in nums.

Input:
nums = [4, 14, 2]

Output:
6

Explanation:
4  = 0100
14 = 1110
2  = 0010
HammingDistance(4,14)=2, (4,2)=2, (14,2)=2  -> 2+2+2 = 6

Example:
Input:  nums = [4, 14, 4]
Output: 4
'''

def totalHammingDistance(nums):
    # Bit trick: count per bit position instead of per pair.
    # For one bit, if `ones` numbers have a 1 there and `zeros = n - ones`
    # have a 0, then every (1,0) pairing differs at that bit: ones * zeros
    # such pairs. Summing this over all 32 bit positions gives the total,
    # turning an O(n^2) pairwise scan into O(32 * n).
    n = len(nums)
    total = 0
    for bit in range(32):
        ones = sum((num >> bit) & 1 for num in nums)
        zeros = n - ones
        total += ones * zeros
    return total


if __name__ == "__main__":
    print(totalHammingDistance([4, 14, 2]))  # Expected: 6
    print(totalHammingDistance([4, 14, 4]))  # Expected: 4


'''
Pattern
Bit Counting (per-bit contribution): for each bit position contribute
ones * zeros to the answer.
Why it works: Hamming distance is additive across bit positions, so the total
over all pairs equals the sum over each bit of how many pairs differ there. At
one bit, only (1,0) pairs differ, and there are exactly ones * zeros of them.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(32 * n)  |  i.e. O(n)
| Space  | O(1)       |

Better Possible?
No. We must read every number's bits at least once; O(32 * n) is optimal and
beats the naive O(n^2) all-pairs approach.
'''
