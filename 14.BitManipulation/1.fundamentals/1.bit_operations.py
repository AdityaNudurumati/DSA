"""
1. Bit Operations Toolkit (Easy)

Problem Statement:
Implement the four fundamental single-bit operations on a 32-bit style integer:
  - set_bit(n, i)    : force bit i to 1
  - clear_bit(n, i)  : force bit i to 0
  - toggle_bit(n, i) : flip bit i
  - check_bit(n, i)  : return the value (0 or 1) of bit i

Bit positions are 0-indexed from the least-significant bit (the rightmost bit).

Example:
  Input:  n = 5            (binary 101)
  Output: set_bit(5, 1)    -> 7   (101 -> 111)
          clear_bit(5, 0)  -> 4   (101 -> 100)
          toggle_bit(5, 2) -> 1   (101 -> 001)
          check_bit(5, 0)  -> 1   (rightmost bit is set)
"""


def set_bit(n, i):
    # OR with a 1 at position i forces that bit to 1, leaves the rest untouched.
    return n | (1 << i)


def clear_bit(n, i):
    # AND with a mask that is all 1s except a 0 at position i clears that bit.
    return n & ~(1 << i)


def toggle_bit(n, i):
    # XOR with a 1 at position i flips that bit (0->1, 1->0).
    return n ^ (1 << i)


def check_bit(n, i):
    # Shift the target bit down to position 0, then mask off everything else.
    return (n >> i) & 1


if __name__ == "__main__":
    print(set_bit(5, 1))     # Expected: 7
    print(clear_bit(5, 0))   # Expected: 4
    print(toggle_bit(5, 2))  # Expected: 1
    print(check_bit(5, 0))   # Expected: 1


"""
Pattern: Bit Fundamentals.

Bit trick & why:
  A single bit is addressed by the mask (1 << i), which has exactly one 1 at
  position i. Combine it with the right boolean operator:
    - OR (|)  sets   : x | 1 = 1, x | 0 = x  -> forces a bit on, others unchanged.
    - AND (&) clears : with the INVERTED mask ~(1 << i) (a single 0), x & 0 = 0,
                       x & 1 = x -> forces one bit off, others unchanged.
    - XOR (^) toggles: x ^ 1 = NOT x, x ^ 0 = x -> flips one bit.
    - Shift+AND reads: (n >> i) brings bit i to the LSB; & 1 isolates it.
  All four are O(1): a single shift plus a single bitwise op, no loops.

| Metric | Value |
| Time   | O(1)  |
| Space  | O(1)  |

Better Possible? No. Each operation is already a constant number of machine-level
bitwise instructions; nothing asymptotically or practically faster exists.
"""
