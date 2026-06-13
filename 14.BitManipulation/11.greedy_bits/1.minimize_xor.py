"""
2429. Minimize XOR (Medium)

Problem Statement
-----------------
Given two positive integers num1 and num2, find the positive integer x such that:
  - x has the same number of set bits as num2 (popcount(x) == popcount(num2)), and
  - the value of x XOR num1 is minimal.

Return x. The answer is guaranteed to be unique for the given constraints.

Example
-------
Input:  num1 = 3,  num2 = 5    Output: 3
Input:  num1 = 1,  num2 = 12   Output: 3
Input:  num1 = 25, num2 = 72   Output: 24
"""


def minimize_xor(num1: int, num2: int) -> int:
    # We must build x with exactly k = popcount(num2) set bits while minimizing x ^ num1.
    # XOR is 0 at a bit position iff x and num1 agree there. To minimize x ^ num1 we want
    # x to match num1 at the HIGHEST-value bits possible (high bits dominate the magnitude).
    #
    # Greedy:
    #   1) Walk num1 from the most significant bit down. Copy each of num1's set bits into x
    #      (so those positions XOR to 0) until we have used up our budget of k set bits.
    #   2) If set bits remain, place them at the LOWEST currently-zero positions of x
    #      (cheapest possible positions to introduce a mismatch).
    k = bin(num2).count("1")  # number of set bits x must have
    result = 0

    # Step 1: copy num1's high set bits while budget remains.
    for i in range(31, -1, -1):
        if k == 0:
            break
        if (num1 >> i) & 1:
            result |= (1 << i)
            k -= 1

    # Step 2: spend leftover set bits on the lowest zero positions.
    for i in range(32):
        if k == 0:
            break
        if not ((result >> i) & 1):
            result |= (1 << i)
            k -= 1

    return result


if __name__ == "__main__":
    print(minimize_xor(3, 5))    # Expected: 3
    print(minimize_xor(1, 12))   # Expected: 3
    print(minimize_xor(25, 72))  # Expected: 24


"""
Pattern
-------
Greedy + Bits. The bit trick: x ^ num1 is minimized by matching num1 on the most
significant bits, because a higher bit contributes more to the value than all lower
bits combined. So with a fixed budget of k = popcount(num2) set bits, greedily mirror
num1's top set bits first (those XOR to 0), then dump any leftover bits into the lowest
free positions (cheapest mismatches). Only the COUNT of set bits in num2 matters, not
its actual value.

| Metric | Value     |
| ------ | --------- |
| Time   | O(W)      |  W = bit width (32). Two linear passes over the bits.
| Space  | O(1)      |  constant extra space.

Better Possible?
----------------
Optimal. The answer is uniquely determined and each of the W bit positions is decided
once, so O(W) time / O(1) space cannot be beaten asymptotically.
"""
