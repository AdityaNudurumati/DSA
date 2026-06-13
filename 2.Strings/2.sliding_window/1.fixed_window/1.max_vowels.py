'''
1. Maximum Number of Vowels in a Substring of Given Length (Medium)
Problem Statement

Given a string s and an integer k, return the maximum number of vowels
(a, e, i, o, u) in any substring of s with length exactly k.

Example
Input:
s = "abciiidef", k = 3

Output:
3
Explanation:
The substring "iii" contains 3 vowels.
'''

def maxVowels(s, k):

    vowels = set("aeiou")
    count = 0          # vowels in the current window
    best = 0

    for right in range(len(s)):

        if s[right] in vowels:      # add the new right char
            count += 1

        if right >= k - 1:
            best = max(best, count)
            if s[right - k + 1] in vowels:   # drop the leftmost char
                count -= 1

    return best


if __name__ == "__main__":
    print(maxVowels("abciiidef", 3))   # Expected: 3
    print(maxVowels("aeiou", 2))       # Expected: 2

'''
Pattern
✅ Fixed-Size Sliding Window

Key Observation
Keep a running count of vowels; on each slide add the entering char and
subtract the leaving char instead of re-scanning the whole window → O(1) per step.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Every character must be inspected at least once.
'''
