"""
190. Reverse Bits (Easy)

Problem Statement:
Reverse the bits of a given 32-bit unsigned integer. Bit i of the input becomes
bit (31 - i) of the output.

Example:
  Input:  n = 43261596    (binary 00000010100101000001111010011100)
  Output: 964176192       (binary 00111001011110000010100101000000)

  Input:  n = 4294967293  (binary 11111111111111111111111111111101)
  Output: 3221225471      (binary 10111111111111111111111111111111)
"""


def reverse_bits(n):
    # Pull bits off the LOW end of n and push them onto the LOW end of result.
    # Shifting result left first makes room; the bit just read lands at the
    # mirrored position after all 32 shifts complete.
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)  # append n's lowest bit to result
        n >>= 1                            # consume that bit from n
    return result


if __name__ == "__main__":
    print(reverse_bits(43261596))    # Expected: 964176192
    print(reverse_bits(4294967293))  # Expected: 3221225471


"""
Pattern: Bit Fundamentals (shift + build).

Bit trick & why:
  Reversal = read the input from the least-significant end while writing to the
  most-significant end. Each step does result = (result << 1) | (n & 1): the
  left shift opens a fresh low slot in result, and (n & 1) drops the current
  lowest input bit into it. After 32 steps, the bit originally at position i has
  been shifted left (31 - i) more times, placing it at position 31 - i -- exactly
  the mirror. n >>= 1 advances to the next input bit.

| Metric | Value     |
| Time   | O(32)=O(1)|
| Space  | O(1)      |

Better Possible? Yes for throughput. The divide-and-conquer swap (exchange
adjacent bits, then pairs, nibbles, bytes, halves using fixed masks like
0x55555555, 0x33333333, 0x0F0F0F0F ...) reverses all 32 bits in ~5 steps
instead of 32. Same O(1) class, fewer operations. The loop shown is the clearest.
"""
