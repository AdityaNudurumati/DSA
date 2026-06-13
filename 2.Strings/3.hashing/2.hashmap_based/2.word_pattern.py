'''
2. Word Pattern (Easy)
Problem Statement

Given a pattern and a string s, return True if s follows the same pattern. Each
letter in pattern must map to exactly one word in s and vice versa (a bijection
between letters and space-separated words).

Example
Input:
pattern = "abba", s = "dog cat cat dog"

Output:
True
'''

def wordPattern(pattern, s):

    words = s.split()

    # length mismatch can never follow the pattern
    if len(pattern) != len(words):
        return False

    char_to_word = {}   # letter -> word
    word_to_char = {}   # word -> letter (enforces one-to-one)

    for c, w in zip(pattern, words):
        if c in char_to_word and char_to_word[c] != w:
            return False
        if w in word_to_char and word_to_char[w] != c:
            return False
        char_to_word[c] = w
        word_to_char[w] = c

    return True


if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat dog"))    # Expected: True
    print(wordPattern("abba", "dog cat cat fish"))   # Expected: False

'''
Pattern
✅ HashMap Based (bijection check)

Key Observation
Same bijection idea as Isomorphic Strings, but mapping letters to whole words.
Two maps guarantee the correspondence is one-to-one in both directions.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
O(n) time is optimal (must scan every word). Space holds the distinct
letter/word mappings.
'''
