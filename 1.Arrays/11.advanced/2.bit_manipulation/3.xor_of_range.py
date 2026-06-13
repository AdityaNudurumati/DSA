'''
3. XOR of a Range (Find XOR of Array) (Easy/Medium)
Problem Statement

Compute the XOR of all integers in a range [L, R] in O(1) using the closed-form
pattern for XOR(0..n). (XOR of an explicit array is just a fold; the interesting
trick is doing a whole range without iterating.)

Example
xor_range(1, 5) = 1^2^3^4^5 = 1
xor_range(4, 8) = 4^5^6^7^8 = 8
'''

def xor_upto(n):
    # XOR of 0..n follows a period-4 pattern in n
    mod = n % 4
    if mod == 0:
        return n
    if mod == 1:
        return 1
    if mod == 2:
        return n + 1
    return 0            # mod == 3


def xor_range(L, R):
    # XOR(L..R) = XOR(0..R) ^ XOR(0..L-1)
    return xor_upto(R) ^ xor_upto(L - 1)


def xor_array(nums):
    # the trivial fold, for completeness
    result = 0
    for x in nums:
        result ^= x
    return result


if __name__ == "__main__":
    print(xor_range(1, 5))                 # Expected: 1
    print(xor_range(4, 8))                 # Expected: 8
    print(xor_array([1, 2, 3, 4, 5]))      # Expected: 1

'''
Pattern
✅ Closed-form XOR(0..n) (period-4 pattern)

Key Observation
XOR(0..n) cycles as n, 1, n+1, 0 for n % 4 == 0,1,2,3. Range XOR is the prefix
trick: XOR(0..R) ^ XOR(0..L-1).

| Metric         | Value |
| -------------- | ----- |
| Range XOR      | O(1)  |
| Array fold     | O(n)  |
| Space          | O(1)  |

Better Possible?
❌ O(1) for the range is optimal.
'''
