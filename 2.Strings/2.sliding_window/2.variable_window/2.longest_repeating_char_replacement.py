'''
2. Longest Repeating Character Replacement (Medium)
Problem Statement

Given a string s and an integer k, you may replace at most k characters with
any uppercase letter. Return the length of the longest substring containing the
same letter you can obtain after at most k replacements.

Example
Input:
s = "ABAB", k = 2

Output:
4
Explanation:
Replace the two 'A's with 'B' (or vice versa) to get "BBBB", length 4.
'''

from collections import defaultdict

def characterReplacement(s, k):

    count = defaultdict(int)   # char frequencies inside the window
    left = 0
    max_freq = 0               # count of the most common char in the window
    best = 0

    for right in range(len(s)):

        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        # chars to replace = window_size - max_freq; window invalid if > k
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))      # Expected: 4
    print(characterReplacement("AABABBA", 1))   # Expected: 4

'''
Pattern
✅ Variable-Size Sliding Window

Key Observation
A window is achievable iff (window_size - count_of_most_frequent_char) <= k,
i.e. the "other" chars can all be replaced. Grow right; shrink left while invalid.

| Metric | Value            |
| ------ | ---------------- |
| Time   | O(n)             |
| Space  | O(1) (<=26 keys) |

Better Possible?
❌ No. Each character is processed a constant number of times.
'''
