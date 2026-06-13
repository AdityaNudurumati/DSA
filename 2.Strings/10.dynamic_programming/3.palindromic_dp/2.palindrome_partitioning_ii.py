'''
2. Palindrome Partitioning II (Hard)
Problem Statement

Given a string s, partition it so that every substring of the partition is a
palindrome. Return the minimum number of cuts needed.

Example

Input:
s = "aab"

Output:
1

Explanation:
One cut "aa" | "b" splits s into two palindromes, so the answer is 1.
'''

def minCut(s):
    n = len(s)
    if n <= 1:
        return 0

    # isPal[i][j] = True if s[i..j] is a palindrome
    isPal = [[False] * n for _ in range(n)]

    # cuts[i] = min cuts needed for prefix s[0..i]
    cuts = [0] * n

    for j in range(n):
        # worst case: cut before every character
        best = j
        for i in range(j + 1):
            # s[i..j] palindrome if ends match and inside is palindrome
            if s[i] == s[j] and (j - i < 2 or isPal[i + 1][j - 1]):
                isPal[i][j] = True
                # if s[i..j] is palindrome, only need a cut before i
                best = 0 if i == 0 else min(best, cuts[i - 1] + 1)
        cuts[j] = best

    return cuts[n - 1]


if __name__ == "__main__":
    print(minCut("aab"))  # Expected: 1
    print(minCut("a"))    # Expected: 0
    print(minCut("ab"))   # Expected: 1


'''
Pattern
✅ Interval palindrome table + prefix DP
First precompute which ranges are palindromes via interval DP, then a 1D
prefix DP finds the minimum cuts: cuts[j] = min over palindromic s[i..j]
of cuts[i-1] + 1.

| Metric | Value   |
| ------ | ------- |
| Time   | O(n^2)  |
| Space  | O(n^2)  |

Better Possible?
Space drops to O(n) using expand-around-center to compute cuts on the fly.
Time O(n^2) is the standard optimal bound here.
'''
