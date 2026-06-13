'''
1. Single Number II (Medium)
Problem Statement

Given an integer array nums where every element appears exactly three times
except for one element which appears exactly once, find and return that single
element.

You must implement a solution with linear runtime complexity and use only
constant extra space.

Input:
nums = [2,2,3,2]

Output:
3

Explanation:
2 appears three times, 3 appears once -> answer is 3.
'''

def singleNumber(nums):
    # Bit trick: count each bit position mod 3.
    # If every number appears 3 times, the sum of any bit across all numbers
    # is a multiple of 3 -> 0 mod 3. The unique number leaves a 1 mod 3 at
    # exactly the bits it has set. We rebuild the answer bit by bit.
    result = 0
    for i in range(32):                       # assume 32-bit signed integers
        bit_sum = 0
        for n in nums:
            bit_sum += (n >> i) & 1            # count 1s at bit i
        if bit_sum % 3:                        # leftover bit belongs to the unique number
            result |= (1 << i)
    # bit 31 is the sign bit: if set, the value is negative in two's complement
    if result >= (1 << 31):
        result -= (1 << 32)
    return result


if __name__ == "__main__":
    print(singleNumber([2, 2, 3, 2]))                          # Expected: 3
    print(singleNumber([0, 1, 0, 1, 0, 1, 99]))                # Expected: 99
    print(singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))    # Expected: -4


'''
Pattern
Bit-counting / mod-3 over bit positions.
Bit trick: sum each bit across all numbers; triples contribute 0 mod 3, so the
remainder at each position reconstructs the lone number. Python ints are
unbounded, so we mask to 32 bits and subtract 2^32 to recover negatives
(two's-complement sign handling).
| Metric | Value     |
| ------ | --------- |
| Time   | O(32 * n) |
| Space  | O(1)      |
Better Possible?
The 32*n pass can be reduced to a single pass using two state masks
(ones, twos): ones ^= x & ~twos; twos ^= x & ~ones. Still O(n) time, O(1)
space, so asymptotically the same but fewer passes.
'''
