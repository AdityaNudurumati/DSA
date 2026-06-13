"""
3. Reverse a String (recursively) (Easy)

Problem Statement:
Given a string s, return the string reversed, using recursion.
An empty string reverses to an empty string.

Example:
    Input:  s = "hello"
    Output: "olleh"
    Input:  s = ""
    Output: ""
"""


def reverse_string(s):
    # Base case: empty (or single-char) string is its own reverse.
    if len(s) <= 1:
        return s
    # Recursive case: reverse the tail, then prepend the first character last.
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))   # Expected: olleh
    print(reverse_string(""))        # Expected:


"""
Pattern: Linear Recursion.
Strip the first character, recursively reverse the remaining substring, then append
the stripped character at the end so it lands in the reversed position.

| Metric | Value |
| Time   | O(n^2) (slicing s[1:] copies O(n) each of n levels) |
| Space  | O(n^2) total slice copies; O(n) recursion stack depth |

Better Possible?
Yes: a two-pointer swap on a list achieves O(n) time and O(1) extra space, or simply
s[::-1]. Passing indices instead of slicing avoids the per-call copy cost.
"""
