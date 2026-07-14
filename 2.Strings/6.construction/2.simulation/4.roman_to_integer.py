'''
4. Roman to Integer (Easy)   [LC13]
Problem Statement

Convert a Roman numeral string to its integer value. Symbols: I=1, V=5, X=10,
L=50, C=100, D=500, M=1000. Normally symbols go large->small and add up, but six
"subtractive" pairs (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900) subtract.

Rule: scan left to right; if a symbol is smaller than the one to its right,
SUBTRACT it, otherwise ADD it.

Example
Input:  "MCMXCIV"
Output: 1994   (M=1000, CM=900, XC=90, IV=4)
'''

def romanToInt(s):

    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    total = 0
    for i in range(len(s)):
        # smaller symbol before a larger one -> it is subtractive
        if i + 1 < len(s) and value[s[i]] < value[s[i + 1]]:
            total -= value[s[i]]
        else:
            total += value[s[i]]
    return total


if __name__ == "__main__":
    print(romanToInt("III"))       # Expected: 3
    print(romanToInt("LVIII"))     # Expected: 58
    print(romanToInt("MCMXCIV"))   # Expected: 1994
    print(romanToInt("IV"))        # Expected: 4

'''
Pattern
✅ String Simulation (one-pass with a look-ahead compare)

Key Observation
The only twist is the subtractive pairs. Comparing each symbol with its right
neighbour handles all six of them without special-casing each pair.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Single linear pass.
'''
