"""
476. Number Complement (Easy)

Problem Statement:
The complement of an integer is the integer you get when you flip all the bits
in its binary representation (within its own bit-length, no leading zeros).
Given a positive integer num, return its complement.

Example:
    Input:  num = 5      (binary 101)
    Output: 2            (binary 010)
    Input:  num = 1      (binary 1)
    Output: 0            (binary 0)
    Input:  num = 10     (binary 1010)
    Output: 5            (binary 0101)
"""


def find_complement(num: int) -> int:
    # We must flip bits ONLY within num's own bit-length, not the full 32/64 bits.
    # Build a mask of all 1s the same width as num: for num = 5 (3 bits) -> 0b111.
    # (1 << bit_length) gives the next power of two (0b1000); subtract 1 -> 0b111.
    # XOR with that full-1 mask flips every in-range bit: 101 ^ 111 = 010 = 2.
    mask = (1 << num.bit_length()) - 1
    return num ^ mask


if __name__ == "__main__":
    print(find_complement(5))   # Expected: 2
    print(find_complement(1))   # Expected: 0
    print(find_complement(10))  # Expected: 5


"""
Pattern: Mathematical Bit Tricks.
Bit trick: XOR with an all-ones mask flips bits. The key is sizing the mask to
num's own width using num.bit_length(): (1 << k) - 1 produces exactly k ones, so
num ^ mask flips every bit within range and leaves no spurious high bits. This
avoids flipping the leading zeros that a fixed-width ~num would touch.

| Metric | Value |
| Time   | O(1)  |
| Space  | O(1)  |

Better Possible? No. bit_length plus a shift, subtract, and XOR are all constant
time; this is the optimal approach.
"""
