"""
371. Sum of Two Integers (Medium)

Problem Statement:
Given two integers a and b, return their sum WITHOUT using the + or -
operators. Use only bitwise operations. Values fit in 32-bit signed range.

Example:
    Input:  a = 1,  b = 2
    Output: 3
    Input:  a = -2, b = 3
    Output: 1
    Input:  a = -1, b = 1
    Output: 0
"""

MASK = 0xFFFFFFFF       # keep computation inside 32 bits
INT_MAX = 0x7FFFFFFF    # 2**31 - 1


def get_sum(a: int, b: int) -> int:
    # XOR gives the "add without carry" result: 1^1=0, 1^0=1, 0^0=0.
    # AND then left-shift by 1 gives the carry: a carry happens only where BOTH
    # bits are 1, and a carry lands in the next-higher position (hence << 1).
    # Repeat until there is no carry left; then XOR alone is the full sum.
    # We mask to 32 bits each step so Python's unbounded ints emulate fixed
    # two's-complement arithmetic (negatives wrap correctly).
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MASK     # sum bits, clipped to 32 bits
        b = carry & MASK       # carry bits to add next round
    # If the top (sign) bit is set, a represents a negative two's-complement
    # number; convert it back to Python's signed value.
    return a if a <= INT_MAX else ~(a ^ MASK)


if __name__ == "__main__":
    print(get_sum(1, 2))   # Expected: 3
    print(get_sum(-2, 3))  # Expected: 1
    print(get_sum(-1, 1))  # Expected: 0


"""
Pattern: Shift Operations.
Bit trick: addition splits into two independent bitwise pieces. XOR produces the
partial sum ignoring carries, while (a & b) << 1 produces the carries shifted
into their next-higher column. Feeding the carry back as the new addend and
repeating until the carry is zero reconstructs ordinary binary addition, exactly
how a ripple-carry adder works in hardware. A 32-bit MASK plus a sign-bit fix-up
makes Python's arbitrary-precision ints behave like fixed-width two's complement,
so negative operands wrap correctly.

| Metric | Value |
| Time   | O(1)  |   # at most 32 carry-propagation rounds for 32-bit ints
| Space  | O(1)  |

Better Possible? No. Without + or -, XOR-sum with shifted-AND carry is the
canonical constant-bound solution; the bounded width caps it at O(1).
"""
