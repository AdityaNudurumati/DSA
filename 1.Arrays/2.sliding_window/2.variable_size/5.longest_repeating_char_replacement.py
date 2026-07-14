'''
5. Longest Repeating Character Replacement (Medium)
Problem Statement

Given a string s (uppercase letters) and an integer k, you may replace AT MOST k
characters with any uppercase letter. Return the length of the longest substring
containing the SAME letter after doing the replacements.

Example
Input:
s = "AABABBA", k = 1

Output:
4
Explanation:
Replace the one 'A' in "ABBA" (or one 'B') to get "BBBB" / "AAAA" of length 4.
'''

def characterReplacement(s, k):

    count = {}
    left = 0
    max_freq = 0          # highest single-letter count seen in the window
    best = 0

    for right in range(len(s)):

        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # chars to replace = window_size - most frequent letter's count
        # if that exceeds k, the window is invalid -> shrink from the left
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(characterReplacement("AABABBA", 1))   # Expected: 4
    print(characterReplacement("ABAB", 2))       # Expected: 4
    print(characterReplacement("AAAA", 0))       # Expected: 4
    print(characterReplacement("", 2))           # Expected: 0

'''
Pattern
✅ Variable-Size Sliding Window (max window with a "replaceable" budget)

Key Observation
A window is valid when (window_length - max_freq) <= k, i.e. the non-majority
letters can all be replaced within the budget k. max_freq is never decreased on
shrink; that's fine because 'best' only ever needs a window LARGER than the
current max, which requires a new, higher max_freq.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n)           |
| Space  | O(1) (<=26 keys)|

Better Possible?
❌ No. Each character is visited by right once and by left once -> O(n).
'''
