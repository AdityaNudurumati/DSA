'''
1. Valid Palindrome (Easy)
Problem Statement

Given a string s, determine whether it is a palindrome.

Ignore:

spaces
punctuation
case differences

Return True if it reads the same forward and backward, otherwise False.

Example
Input:
s = "A man, a plan, a canal: Panama"

Output:
True
Explanation:
"amanaplanacanalpanama" reads the same both ways.
'''

def isPalindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        # skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # compare ignoring case
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(isPalindrome("race a car"))                      # Expected: False

'''
Pattern
Opposite Ends Two Pointers — walk inward from both sides, skipping junk,
comparing mirrored characters. No extra string is built.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No — every character may need to be examined once.
'''
