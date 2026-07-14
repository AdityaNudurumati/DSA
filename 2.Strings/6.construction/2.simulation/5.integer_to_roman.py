'''
5. Integer to Roman (Medium)   [LC12]
Problem Statement

Convert an integer (1..3999) to its Roman numeral string. Greedily subtract the
largest possible value token, appending its symbol, until the number is 0. The
subtractive forms (CM, CD, XC, XL, IX, IV) are included as their own tokens so a
single greedy pass produces the canonical numeral.

Example
Input:  1994
Output: "MCMXCIV"
'''

def intToRoman(num):

    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    out = []
    for v, sym in zip(vals, syms):
        while num >= v:          # take as many of this token as fit
            out.append(sym)
            num -= v
    return "".join(out)


if __name__ == "__main__":
    print(intToRoman(3))       # Expected: III
    print(intToRoman(58))      # Expected: LVIII
    print(intToRoman(1994))    # Expected: MCMXCIV
    print(intToRoman(4))       # Expected: IV

'''
Pattern
✅ Greedy + String Construction (largest-token-first)

Key Observation
Including the six subtractive pairs as first-class tokens turns Roman construction
into a plain greedy: always take the biggest token that still fits. No backtracking.

| Metric | Value |
| ------ | ----- |
| Time   | O(1)  (at most 13 tokens, bounded input) |
| Space  | O(1)  |

Better Possible?
❌ No. The token table makes it effectively constant work.
'''
