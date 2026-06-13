'''
89. Gray Code (Medium)
Problem Statement

An n-bit gray code sequence is a sequence of 2^n integers where:
- Every integer is in the inclusive range [0, 2^n - 1],
- The first integer is 0,
- An integer appears no more than once in the sequence,
- The binary representation of every pair of ADJACENT integers differs by
  exactly one bit, and
- The binary representation of the FIRST and LAST integers also differs by
  exactly one bit (the sequence is cyclic).

Given an integer n, return any valid n-bit gray code sequence.

Input:
n = 2

Output:
[0, 1, 3, 2]

Explanation:
The binary representation is [00, 01, 11, 10].
- 00 and 01 differ by one bit.
- 01 and 11 differ by one bit.
- 11 and 10 differ by one bit.
- 10 and 00 (last and first) differ by one bit.
'''

def grayCode(n):
    # Reflected binary gray code: the i-th value is  i ^ (i >> 1).
    # Why it works: XOR-ing i with itself shifted right by one flips a bit only
    # where consecutive bits of i differ. Going from i to i+1 in binary changes a
    # trailing run of bits, but after the i ^ (i>>1) folding exactly ONE output
    # bit ends up flipping each step -> the one-bit-change (and cyclic) property.
    return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == "__main__":
    print(grayCode(2))  # Expected: [0, 1, 3, 2]
    print(grayCode(1))  # Expected: [0, 1]
    print(grayCode(3))  # Expected: [0, 1, 3, 2, 6, 7, 5, 4]


'''
Pattern
✅ Gray Code  (reflected binary code via  i ^ (i >> 1))

The bit trick: map each index i in [0, 2^n) to  i ^ (i >> 1).
This is the standard binary-to-gray conversion. Each increment of i flips one
output bit, so adjacent values differ by a single bit; because the construction
is reflective, the last and first also differ by one bit, making it cyclic.
The order of this output IS guaranteed by the formula, so no sorting is applied.

| Metric | Value  |
| ------ | ------ |
| Time   | O(2^n) |
| Space  | O(2^n) |   (output only; O(1) extra)

Better Possible?
❌ No
There are 2^n integers to emit, so any algorithm must do at least O(2^n) work.
The formula produces each element in O(1), so this is optimal.
'''
