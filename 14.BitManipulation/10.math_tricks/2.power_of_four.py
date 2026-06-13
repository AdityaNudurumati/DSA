"""
342. Power of Four (Easy)

Problem Statement:
Given an integer n, return True if it is a power of four, otherwise False.
An integer n is a power of four if there exists an integer x such that n == 4**x.

Example:
    Input:  n = 16
    Output: True          (4**2)
    Input:  n = 5
    Output: False
    Input:  n = 1
    Output: True          (4**0)
    Input:  n = 8
    Output: False         (power of two but the set bit is at an odd position)
"""


def is_power_of_four(n: int) -> bool:
    # Step 1: must be a power of two -> exactly one set bit -> n & (n-1) == 0.
    # Step 2: powers of four are 1, 4, 16, 64... their single set bit always
    #         lands at an EVEN bit index (0, 2, 4, 6...). Powers of two that are
    #         NOT powers of four (2, 8, 32...) have their bit at an odd index.
    # The mask 0x55555555 = 0101...0101 has 1s only at even positions, so the
    # set bit survives the AND iff it sits at an even position.
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


if __name__ == "__main__":
    print(is_power_of_four(16))  # Expected: True
    print(is_power_of_four(5))   # Expected: False
    print(is_power_of_four(1))   # Expected: True
    print(is_power_of_four(8))   # Expected: False


"""
Pattern: Mathematical Bit Tricks.
Bit trick: combine the power-of-two test (single set bit via n & (n-1) == 0) with
a position test. The hex mask 0x55555555 keeps only the even-indexed bits; a
power of four's lone set bit lives at an even index, while a non-four power of two
(2, 8, 32, ...) sits at an odd index and is masked away. Both checks together are
O(1) with no loops.

| Metric | Value |
| Time   | O(1)  |
| Space  | O(1)  |

Better Possible? No. Two constant-time bitwise checks; asymptotically optimal.
"""
