'''
2. String to Integer (atoi) (Medium)
Problem Statement

Implement the myAtoi function which converts a string to a 32-bit signed
integer, following these steps:
1. Skip leading whitespace.
2. Read an optional single '+' or '-' sign.
3. Read in the digits until a non-digit character or the end is reached.
4. Convert those digits to an integer (0 if there were none).
5. Clamp the result to the 32-bit signed range
   [-2^31, 2^31 - 1] = [-2147483648, 2147483647].

Example
Input:
s = "   -42"

Output:
-42
'''

def myAtoi(s):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    i, n = 0, len(s)

    # 1. skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    # 2. optional sign
    sign = 1
    if i < n and s[i] in '+-':
        if s[i] == '-':
            sign = -1
        i += 1

    # 3. read digits, building the number without int()
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + (ord(s[i]) - ord('0'))
        i += 1

    num *= sign

    # 5. clamp to 32-bit signed range
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num


if __name__ == "__main__":
    print(myAtoi("42"))               # Expected: 42
    print(myAtoi("   -42"))           # Expected: -42
    print(myAtoi("4193 with words"))  # Expected: 4193
    print(myAtoi("words and 987"))    # Expected: 0


'''
Pattern
✅ Encoding/Decoding (parse text -> value, state-by-state)
A small linear scan: skip space, read sign, accumulate digits, then clamp.
The key is handling each stage in strict order and stopping at the first
invalid character.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No — must scan the relevant prefix of the input once.
'''
