'''
3. Add Binary (Easy)
Problem Statement

Given two binary strings a and b, return their sum as a binary string.

Each string contains only the characters '0' and '1'. Do the addition
digit-by-digit (no int(x, 2)).

Example
Input:
a = "11"
b = "1"

Output:
"100"
'''

def addBinary(a, b):
    i = len(a) - 1          # least-significant bit of a
    j = len(b) - 1          # least-significant bit of b
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        bit1 = ord(a[i]) - ord('0') if i >= 0 else 0
        bit2 = ord(b[j]) - ord('0') if j >= 0 else 0

        total = bit1 + bit2 + carry
        carry = total // 2          # base 2 carry
        result.append(chr(total % 2 + ord('0')))

        i -= 1
        j -= 1

    return ''.join(reversed(result))


if __name__ == "__main__":
    print(addBinary("11", "1"))         # Expected: 100
    print(addBinary("1010", "1011"))    # Expected: 10101


'''
Pattern
✅ String Builder (digit-by-digit addition, base 2)
Same as decimal add-strings but the carry threshold is 2 instead of 10.

| Metric | Value        |
| ------ | ------------ |
| Time   | O(max(n, m)) |
| Space  | O(max(n, m)) |

Better Possible?
❌ No — must read each bit at least once.
'''
