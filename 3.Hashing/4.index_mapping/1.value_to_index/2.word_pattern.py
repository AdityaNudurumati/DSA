'''
2. Word Pattern (Easy)
Problem Statement

Given a pattern string and a string s of space-separated words, return True if s
follows the same pattern. "Follows" means there is a bijection between each character
in pattern and each word in s: every character maps to exactly one word and every word
maps back to exactly one character.

Example
Input:
pattern = "abba", s = "dog cat cat dog"

Output:
True
Explanation:
'a' <-> "dog" and 'b' <-> "cat" consistently, forming a one-to-one correspondence.
'''

def wordPattern(pattern, s):

    words = s.split()

    # lengths must match: one char per word
    if len(pattern) != len(words):
        return False

    char_to_word = {}               # forward map: pattern char -> word
    word_to_char = {}               # reverse map: word -> pattern char (guards bijection)

    for c, w in zip(pattern, words):
        # seen this char: its word must still match
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        # this word already bound to a different char: not one-to-one
        elif w in word_to_char:
            return False
        else:
            char_to_word[c] = w
            word_to_char[w] = c

    return True


if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat dog"))     # Expected: True
    print(wordPattern("abba", "dog cat cat fish"))    # Expected: False

'''
Pattern
✅ Value -> value mapping (two dicts enforce a char<->word bijection)

Key Observation
Same shape as Isomorphic Strings but the "value" on one side is a whole word. Two maps
guarantee both directions: a char never maps to two words and a word never binds to two
chars. A pre-check on lengths rules out the trivial size mismatch.

| Metric | Value |
| ------ | ----- |
| Time   | O(n + m)  (n = pattern length, m = total chars in s) |
| Space  | O(k)      (k = distinct chars/words) |

Better Possible?
Linear in the input size is optimal — every char and word must be read at least once.
'''
