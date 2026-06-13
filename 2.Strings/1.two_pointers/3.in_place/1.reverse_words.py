'''
1. Reverse Words in a String (Medium)
Problem Statement

Given a string s, reverse the order of the words. A word is a maximal
sequence of non-space characters. The words in s are separated by one or
more spaces.

Return a string with the words in reverse order, joined by a single space,
with no leading or trailing spaces.

Example
Input:
s = "the sky is blue"

Output:
"blue is sky the"
'''

def reverseWords(s):

    words = []
    i = 0
    n = len(s)

    # two-pointer scan: skip spaces, then capture a full word
    while i < n:
        while i < n and s[i] == " ":
            i += 1
        if i >= n:
            break
        start = i
        while i < n and s[i] != " ":
            i += 1
        words.append(s[start:i])   # one word

    # reverse the collected words and join with single spaces
    words.reverse()
    return " ".join(words)


if __name__ == "__main__":
    print(reverseWords("the sky is blue"))      # Expected: blue is sky the
    print(reverseWords("  hello world  "))      # Expected: world hello

'''
Pattern
In-place Processing (two-pointer word scan) — a read pointer walks the string,
skipping runs of spaces and slicing out each word; words are then reversed.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (word list / output)

Better Possible?
No — the whole string must be read; O(n) is optimal.
'''
