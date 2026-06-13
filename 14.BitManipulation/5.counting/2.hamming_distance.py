'''
2. Hamming Distance (Easy)
Problem Statement

The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Input:
x = 1, y = 4

Output:
2

Explanation:
1 = 0 0 1
4 = 1 0 0
        ^   ^   (bit 0 and bit 2 differ) -> distance 2

Example:
Input:  x = 3, y = 1
Output: 1
'''

def hammingDistance(x, y):
    # Bit trick: x ^ y has a 1 exactly where x and y differ, so the answer is
    # popcount(x ^ y). We count set bits with Brian Kernighan: z &= z - 1 clears
    # the lowest set bit, looping once per set bit.
    z = x ^ y
    count = 0
    while z:
        z &= z - 1
        count += 1
    return count


if __name__ == "__main__":
    print(hammingDistance(1, 4))  # Expected: 2
    print(hammingDistance(3, 1))  # Expected: 1


'''
Pattern
Bit Counting via XOR: differing bits = popcount(x ^ y).
Why it works: XOR yields 1 only where the two inputs disagree; counting those
1s (Brian Kernighan: z &= z - 1) gives exactly the number of differing positions.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(k)           |  k = number of set bits in x ^ y (<= 32)
| Space  | O(1)           |

Better Possible?
No. A single XOR plus a popcount is optimal; Kernighan touches only set bits.
'''
