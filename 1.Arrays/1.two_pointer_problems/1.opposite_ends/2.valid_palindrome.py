'''
4. Valid Palindrome (Easy)
Problem Statement

Given a string s, determine whether it is a palindrome.

Ignore:

spaces
punctuation
case differences

Return True if it is a palindrome, otherwise False.
Input:
s = "A man, a plan, a canal: Panama"

Output:
True
Explanation:
amanaplanacanalpanama

which reads the same forward and backward.
'''

def isPalindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

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
✅ Opposite Direction Two Pointers

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No

Need to examine characters.
'''