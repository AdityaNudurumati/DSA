'''
2. Backspace String Compare (Easy)
Problem Statement

Given two strings s and t, return True if they are equal when both are typed
into empty text editors, where '#' means a backspace character.

Note that backspacing on empty text does nothing.

Example
Input:
s = "ab#c", t = "ad#c"

Output:
True
Explanation:
Both become "ac".
'''

def backspaceCompare(s, t):

    def nextValid(string, index):
        # walk backwards, honoring '#' as a skip, return next real char index
        skip = 0
        while index >= 0:
            if string[index] == "#":
                skip += 1
            elif skip > 0:
                skip -= 1          # this char was deleted by a backspace
            else:
                break              # a surviving character
            index -= 1
        return index

    i = len(s) - 1
    j = len(t) - 1

    # compare from the back so we never build the result string (O(1) space)
    while i >= 0 or j >= 0:
        i = nextValid(s, i)
        j = nextValid(t, j)

        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False           # one ran out before the other

        i -= 1
        j -= 1

    return True


if __name__ == "__main__":
    print(backspaceCompare("ab#c", "ad#c"))  # Expected: True
    print(backspaceCompare("a##c", "#a#c"))  # Expected: True
    print(backspaceCompare("a#c", "b"))      # Expected: False

'''
Pattern
Same Direction Two Pointers (scanning backward) — each pointer skips deleted
characters using a backspace counter, then surviving chars are compared.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No — O(1) space back-scan is optimal; a stack would cost O(n) space.
'''
