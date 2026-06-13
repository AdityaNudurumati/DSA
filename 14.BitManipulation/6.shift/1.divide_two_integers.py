"""
29. Divide Two Integers (Medium)

Problem Statement:
Given two integers dividend and divisor, divide them WITHOUT using
multiplication, division, or the mod operator. The result is truncated toward
zero (drop the fractional part). Assume a 32-bit signed integer range
[-2**31, 2**31 - 1]; if the quotient overflows, clamp it to 2**31 - 1.

Example:
    Input:  dividend = 10, divisor = 3
    Output: 3              (10 / 3 = 3.33..., truncated to 3)
    Input:  dividend = 7,  divisor = -3
    Output: -2             (7 / -3 = -2.33..., truncated to -2)
    Input:  dividend = -2147483648, divisor = -1
    Output: 2147483647     (true answer 2**31 overflows, clamp to 2**31 - 1)
"""

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


def divide(dividend: int, divisor: int) -> int:
    # Only overflow case: INT_MIN / -1 = 2**31, which is out of range -> clamp.
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Work with non-negative magnitudes; track sign separately.
    negative = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)

    quotient = 0
    # Repeatedly subtract the LARGEST shifted divisor (b << k) that still fits.
    # b << k == b * 2^k, and the matching chunk of quotient is 1 << k == 2^k.
    # Each outer pass removes the top "binary digit" of the quotient, so the
    # whole division finishes in O(log a) shift/subtract steps instead of O(a).
    while a >= b:
        temp, multiple = b, 1
        while a >= (temp << 1):
            temp <<= 1        # double the divisor: b * 2^(k+1)
            multiple <<= 1     # double the accumulated quotient chunk
        a -= temp              # subtract the biggest fitting chunk
        quotient += multiple

    return -quotient if negative else quotient


if __name__ == "__main__":
    print(divide(10, 3))            # Expected: 3
    print(divide(7, -3))            # Expected: -2
    print(divide(-2147483648, -1))  # Expected: 2147483647


"""
Pattern: Shift Operations.
Bit trick: left-shifting the divisor (b << k) multiplies it by 2^k, so we can
peel the quotient off one binary digit at a time. On each pass we double the
divisor while it still fits in the remaining dividend, subtract that largest
chunk, and add the matching 1 << k to the quotient. Because each chunk at least
halves the remaining work, we touch O(log dividend) chunks rather than looping a
single subtraction billions of times. Sign is handled on magnitudes, and the
lone INT_MIN / -1 overflow is clamped up front.

| Metric | Value      |
| Time   | O(log n)   |
| Space  | O(1)       |

Better Possible? No. Without using * / %, the doubling-and-subtract scheme is
the standard optimum; you cannot beat O(log n) chunk removals for this constraint.
"""
