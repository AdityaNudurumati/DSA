'''
3. Reverse Words in a String III (Easy)
Problem Statement

Given a string s, reverse the characters of each word while preserving
whitespace and the original word order.

Example
Input:
s = "Let's take LeetCode contest"

Output:
"s'teL ekat edoCteeL tsetnoc"
'''

def reverseWords(s):

    chars = list(s)
    n = len(chars)
    start = 0

    # find each word [start, end) then reverse it in place with two pointers
    for i in range(n + 1):
        if i == n or chars[i] == " ":
            left = start
            right = i - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            start = i + 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverseWords("Let's take LeetCode contest"))
    # Expected: s'teL ekat edoCteeL tsetnoc

'''
Pattern
In-place Processing (opposite-end swap per word) — detect word boundaries on a
single forward scan, then reverse each word with a left/right swap loop.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (char list; O(1) extra if the buffer is mutable)

Better Possible?
No — each character is swapped at most once.
'''
