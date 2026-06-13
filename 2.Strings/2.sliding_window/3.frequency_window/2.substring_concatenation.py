'''
2. Substring with Concatenation of All Words (Hard)
Problem Statement

Given a string s and a list words of equal-length strings, return the start
indices of substrings of s that are a concatenation of every word in words
exactly once, in any order, with no characters in between.

Example
Input:
s = "barfoothefoobarman", words = ["foo", "bar"]

Output:
[0, 9]
Explanation:
At index 0 "barfoo" = "bar"+"foo"; at index 9 "foobar" = "foo"+"bar".
'''

from collections import Counter

def findSubstring(s, words):

    if not words or not s:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total = word_len * num_words        # length of a full concatenation
    if total > len(s):
        return []

    need = Counter(words)               # required word frequencies
    result = []

    # try each possible alignment offset (0 .. word_len-1)
    for offset in range(word_len):
        left = offset
        count = 0                       # words matched in current window
        window = Counter()

        for right in range(offset, len(s) - word_len + 1, word_len):

            word = s[right:right + word_len]    # next word-sized chunk

            if word in need:
                window[word] += 1
                count += 1

                # too many of this word -> shrink from the left
                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == num_words:          # full match window
                    result.append(left)
            else:
                window.clear()                  # broken chunk -> reset window
                count = 0
                left = right + word_len

    return result


if __name__ == "__main__":
    print(sorted(findSubstring("barfoothefoobarman", ["foo", "bar"])))   # Expected: [0, 9]

'''
Pattern
✅ Frequency Window (word-level fixed window)

Key Observation
Because every word has the same length, scan s in word-sized chunks. Run a
sliding window for each of the word_len start offsets, keeping a word-count map.

| Metric | Value                       |
| ------ | --------------------------- |
| Time   | O(n * word_len)             |
| Space  | O(num_words * word_len)     |

Better Possible?
❌ Not asymptotically. The offset loop keeps it near-linear in practice.
'''
