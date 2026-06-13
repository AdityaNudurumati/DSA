'''
4. Longest Substring with At Most K Distinct Characters (Medium)
Problem Statement

Given a string s and an integer k, return the length of the longest substring
that contains at most k distinct characters.

Example
Input:
s = "eceba", k = 2

Output:
3
Explanation:
"ece" has 2 distinct characters, length 3.
'''

def lengthOfLongestSubstringKDistinct(s, k):

    if k == 0:
        return 0

    count = {}          # char -> count in window
    left = 0
    best = 0

    for right, ch in enumerate(s):

        count[ch] = count.get(ch, 0) + 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(lengthOfLongestSubstringKDistinct("eceba", 2))   # Expected: 3
    print(lengthOfLongestSubstringKDistinct("aa", 1))       # Expected: 2
    print(lengthOfLongestSubstringKDistinct("abcadcacacaca", 3))  # Expected: 11

'''
Pattern
✅ Variable-Size Sliding Window (at most K distinct) — generalizes Fruits Into Baskets

| Metric | Value    |
| ------ | -------- |
| Time   | O(n)     |
| Space  | O(k)     |

Better Possible?
❌ No.
'''
