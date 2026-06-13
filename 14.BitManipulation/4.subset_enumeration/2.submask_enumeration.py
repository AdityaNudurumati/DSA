'''
2. Submask Enumeration (Medium)
Problem Statement

Given a bitmask `mask`, enumerate all of its submasks. A submask `sub` is any
value whose set bits are a subset of mask's set bits, i.e. (sub & mask) == sub.

Return all submasks of mask (including 0 and mask itself). The order is not
guaranteed, so we sort the result before printing.

Input:
mask = 0b101  (= 5)

Output:
[0, 1, 4, 5]

Explanation:
mask = 101. Its set bits are positions 0 and 2, so every submask only uses those
bits: 000=0, 001=1, 100=4, 101=5.
'''

def submasks(mask):
    result = []
    sub = mask
    # Bit trick: sub = (sub - 1) & mask walks DOWN through every submask.
    # Subtracting 1 flips the lowest set bit off and turns lower zeros to ones;
    # AND-ing with mask keeps only bits allowed by mask, so we land on the next
    # smaller submask. We must handle 0 separately because the loop stops at it.
    while sub > 0:
        result.append(sub)
        sub = (sub - 1) & mask
    result.append(0)  # the empty submask
    return result


if __name__ == "__main__":
    mask1 = 0b101  # = 5
    # Sort so the order matches the Expected output.
    print(sorted(submasks(mask1)))  # Expected: [0, 1, 4, 5]

    mask2 = 0b11   # = 3
    print(sorted(submasks(mask2)))  # Expected: [0, 1, 2, 3]


'''
Pattern
✅ Submask Enumeration
To visit every subset of a fixed set of bits, start from `mask` itself and repeat
sub = (sub - 1) & mask. This skips directly from one submask to the next without
scanning the masks in between. Summed over all masks of an n-bit universe the
total work is O(3^n): each of the n bit positions is independently "in mask and
in sub", "in mask not in sub", or "not in mask" -> 3^n combinations.

| Metric | Value                                  |
| ------ | -------------------------------------- |
| Time   | O(2^k), k = number of set bits in mask |
| Space  | O(2^k) to store the result             |

Better Possible?
❌ No
A mask with k set bits has exactly 2^k submasks, so we must emit 2^k values.
The (sub - 1) & mask iteration touches each submask exactly once, which is
optimal; iterating 0..2^n and filtering would be the slower O(2^n) approach.
'''
