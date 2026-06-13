'''
3. Reverse String (Easy)
Problem Statement

Given an array of characters s, reverse it in-place.

You must do this by modifying the input array using O(1) extra memory.

Example
Input:
s = ["h","e","l","l","o"]

Output:
["o","l","l","e","h"]
'''

def reverseString(s):

    left = 0
    right = len(s) - 1

    while left < right:
        # swap the mirrored characters, then close in
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)  # Expected: ['o', 'l', 'l', 'e', 'h']

'''
Pattern
Opposite Ends Two Pointers — swap the outermost pair and move both pointers
inward until they meet.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No — each character is touched once and swapped in place.
'''
