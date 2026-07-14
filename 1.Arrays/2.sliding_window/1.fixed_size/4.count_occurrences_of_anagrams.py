'''
4. Count Occurrences of Anagrams (Medium)
Problem Statement

Given a text string and a pattern string, count how many substrings of text are
ANAGRAMS of pattern (same letters with the same frequencies, any order).

Example
Input:
text = "forxxorfxdofr", pattern = "for"

Output:
3
Explanation:
"for" (index 0), "orf" (index 4), "ofr" (index 10) are anagrams of "for".
'''

from collections import Counter

def countAnagrams(text, pattern):

    k = len(pattern)
    if k > len(text):
        return 0

    need = Counter(pattern)     # target letter frequencies
    window = Counter()          # letter frequencies in the current window
    count = 0

    for i in range(len(text)):

        window[text[i]] += 1                # add the entering char

        if i >= k:                          # window too big -> drop leftmost
            left_char = text[i - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]       # keep the map clean for == compare

        if i >= k - 1 and window == need:   # full window matches the pattern
            count += 1

    return count


if __name__ == "__main__":
    print(countAnagrams("forxxorfxdofr", "for"))   # Expected: 3
    print(countAnagrams("aabaabaa", "aaba"))         # Expected: 4
    print(countAnagrams("cbaebabacd", "abc"))        # Expected: 2
    print(countAnagrams("abc", "abcd"))              # Expected: 0

'''
Pattern
✅ Fixed-Size Sliding Window + Frequency Map

Key Observation
A substring is an anagram of pattern exactly when its letter-count map equals the
pattern's map. Slide a window of width k: add the entering char, drop the leaving
char, and compare the two maps. Deleting zero-count keys keeps the "==" check
correct in O(alphabet).

| Metric | Value                    |
| ------ | ------------------------ |
| Time   | O(n) (26-key map compare)|
| Space  | O(1) (<=26 keys)         |

Better Possible?
❌ No. Every character enters and leaves the window once -> O(n).
'''
