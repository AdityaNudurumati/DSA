'''
2. Multiply Strings (Medium)
Problem Statement

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

You must not use any built-in BigInteger library or convert the inputs to
integers directly.

Example
Input:
num1 = "2"
num2 = "3"

Output:
"6"
'''

def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    n, m = len(num1), len(num2)
    # digit i of num1 times digit j of num2 lands in positions i+j and i+j+1
    res = [0] * (n + m)

    # grade-school multiplication, least-significant digits first
    for i in range(n - 1, -1, -1):
        d1 = ord(num1[i]) - ord('0')
        for j in range(m - 1, -1, -1):
            d2 = ord(num2[j]) - ord('0')

            mul = d1 * d2 + res[i + j + 1]  # add what's already there
            res[i + j + 1] = mul % 10       # low digit stays
            res[i + j] += mul // 10         # carry into higher column

    # build the string, skipping a leading zero if present
    start = 0
    while start < len(res) - 1 and res[start] == 0:
        start += 1

    return ''.join(chr(d + ord('0')) for d in res[start:])


if __name__ == "__main__":
    print(multiply("2", "3"))        # Expected: 6
    print(multiply("123", "456"))    # Expected: 56088
    print(multiply("0", "52"))       # Expected: 0


'''
Pattern
✅ String Builder (grade-school multiplication on a digit buffer)
Digit i of num1 times digit j of num2 contributes to positions i+j and
i+j+1 of the result buffer; accumulate carries, then join.

| Metric | Value    |
| ------ | -------- |
| Time   | O(n * m) |
| Space  | O(n + m) |

Better Possible?
❌ Not for the schoolbook method. FFT-based multiplication exists
(O((n+m) log(n+m))) but is overkill for interview-sized inputs.
'''
