'''
1. Add Strings (Easy)
Problem Statement

Given two non-negative integers num1 and num2 represented as strings,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling
large integers (such as BigInteger) and without converting the inputs to
integers directly (no int()).

Example
Input:
num1 = "11"
num2 = "123"

Output:
"134"
'''

def addStrings(num1, num2):
    i = len(num1) - 1          # start at least-significant digit of num1
    j = len(num2) - 1          # start at least-significant digit of num2
    carry = 0
    result = []                # accumulate digits, join at the end

    while i >= 0 or j >= 0 or carry:
        # ord('x') - ord('0') converts a digit char to its value without int()
        d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

        total = d1 + d2 + carry
        carry = total // 10            # carry forward to next column
        result.append(chr(total % 10 + ord('0')))  # digit back to char

        i -= 1
        j -= 1

    # we built it least-significant-first, so reverse before joining
    return ''.join(reversed(result))


if __name__ == "__main__":
    print(addStrings("11", "123"))  # Expected: 134
    print(addStrings("456", "77"))  # Expected: 533


'''
Pattern
✅ String Builder (digit-by-digit grade-school addition)
Process from the least significant end, carry forward, accumulate chars
in a list and "".join at the end (Python strings are immutable).

| Metric | Value           |
| ------ | --------------- |
| Time   | O(max(n, m))    |
| Space  | O(max(n, m))    |

Better Possible?
❌ No — every digit must be read at least once; this is optimal.
'''
