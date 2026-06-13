"""
191. Number of 1 Bits / Hamming Weight (Easy)

Problem Statement:
Given an unsigned integer n, return the number of '1' bits it has in its binary
representation (also known as the Hamming weight).

Example:
  Input:  n = 11           (binary 1011)
  Output: 3                (three set bits)

  Input:  n = 128          (binary 10000000)
  Output: 1

  Input:  n = 4294967293   (binary 11111111111111111111111111111101)
  Output: 31
"""


def hamming_weight(n):
    # Brian Kernighan's algorithm: n & (n - 1) clears the LOWEST set bit.
    # Each iteration removes exactly one 1-bit, so the loop runs once per set bit.
    count = 0
    while n:
        n &= n - 1   # drop the lowest set bit
        count += 1
    return count


if __name__ == "__main__":
    print(hamming_weight(11))          # Expected: 3
    print(hamming_weight(128))         # Expected: 1
    print(hamming_weight(4294967293))  # Expected: 31


"""
Pattern: Bit Fundamentals (bit counting / popcount).

Bit trick & why:
  Subtracting 1 from n flips the lowest set bit to 0 and turns every 0 below it
  into a 1. ANDing n with (n - 1) therefore clears precisely that lowest set bit
  and leaves all higher bits intact. Repeating until n == 0 counts the set bits
  in time proportional to the NUMBER of 1s (not the total bit width), which beats
  the naive "test all 32 bits" approach when the value is sparse.

| Metric | Value                              |
| Time   | O(k), k = number of set bits (<=32)|
| Space  | O(1)                               |

Better Possible? Marginally. A fixed bit-width loop is O(32) = O(1). The true
constant-time option is a hardware popcount (Python's int.bit_count() in 3.10+,
or bin(n).count("1")). Kernighan is the classic interview-grade manual method.
"""
