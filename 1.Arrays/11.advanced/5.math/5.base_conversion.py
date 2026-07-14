'''
5. Base Conversion (Easy)
Problem Statement

Convert a non-negative integer to its string representation in an arbitrary base
b (2 <= b <= 16), and parse such a string back to an integer. This is the general
"divide by base, collect remainders" routine that underlies binary/hex/base-7
(LC504) and to-hex (LC405) style problems.

Example
Input:  n = 100, base = 16   ->  "64"
Input:  s = "64", base = 16  ->  100
'''

DIGITS = "0123456789ABCDEF"

def to_base(n, base):
    if n == 0:
        return "0"
    out = []
    while n > 0:
        out.append(DIGITS[n % base])   # least-significant digit first
        n //= base
    return "".join(reversed(out))       # reverse for most-significant first


def from_base(s, base):
    value = 0
    for ch in s:
        value = value * base + DIGITS.index(ch)   # Horner's rule
    return value


if __name__ == "__main__":
    print(to_base(100, 16))    # Expected: 64
    print(to_base(100, 2))     # Expected: 1100100
    print(to_base(7, 7))       # Expected: 10
    print(to_base(0, 2))       # Expected: 0

    print(from_base("64", 16)) # Expected: 100
    print(from_base("1100100", 2))  # Expected: 100
    print(from_base("10", 7))  # Expected: 7

'''
Pattern
✅ Base Conversion (repeated division / Horner's rule)

Key Observation
to_base: repeatedly take n % base (a digit) and n //= base until 0, then reverse.
from_base: fold digits left to right as value*base + digit. Same idea powers
binary, hex, base-7, and Excel-column conversions.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(log_base n)  |
| Space  | O(log_base n)  |

Better Possible?
❌ No. Proportional to the number of output digits.
'''
