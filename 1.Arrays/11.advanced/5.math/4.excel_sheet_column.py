'''
4. Excel Sheet Column Number / Title (Easy)   [LC171 / LC168]
Problem Statement

Excel columns are labelled A, B, ..., Z, AA, AB, ..., ZZ, AAA, ... This is a
BIJECTIVE base-26 system (there is no "zero" digit).

  titleToNumber("AB") -> 28     (column title  -> number)
  convertToTitle(28)  -> "AB"    (number       -> column title)

Example
Input:  "ZY"      Output: 701
Input:  701       Output: "ZY"
'''

def titleToNumber(s):
    # like base-26 with A=1..Z=26 (no zero digit)
    result = 0
    for c in s:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result


def convertToTitle(n):
    # bijective base-26: subtract 1 each step so 1..26 map to A..Z
    out = []
    while n > 0:
        n -= 1
        out.append(chr(n % 26 + ord('A')))
        n //= 26
    return "".join(reversed(out))


if __name__ == "__main__":
    print(titleToNumber("A"))     # Expected: 1
    print(titleToNumber("AB"))    # Expected: 28
    print(titleToNumber("ZY"))    # Expected: 701

    print(convertToTitle(1))      # Expected: A
    print(convertToTitle(28))     # Expected: AB
    print(convertToTitle(701))    # Expected: ZY

'''
Pattern
✅ Base Conversion (bijective base-26, no zero digit)

Key Observation
Standard base-26 has digits 0..25, but Excel has 1..26 with no zero. The "n -= 1"
before each digit shifts the system so 26 maps to 'Z' instead of rolling over to
"A0". Reading a title is normal Horner's-rule base conversion.

| Metric | Value    |
| ------ | -------- |
| Time   | O(len)   |
| Space  | O(len)   |

Better Possible?
❌ No. Linear in the number of digits.
'''
