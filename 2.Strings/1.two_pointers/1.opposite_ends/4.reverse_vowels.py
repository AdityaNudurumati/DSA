'''
4. Reverse Vowels of a String (Easy)
Problem Statement

Given a string s, reverse only the vowels in it and return the result.
The vowels are a, e, i, o, u (both lower and upper case). All other
characters stay in their original positions.

Example
Input:
s = "hello"

Output:
"holle"
Explanation:
The vowels 'e' and 'o' are swapped.
'''

def reverseVowels(s):

    vowels = set("aeiouAEIOU")
    chars = list(s)            # strings are immutable, work on a list

    left = 0
    right = len(chars) - 1

    while left < right:

        # move left to the next vowel
        while left < right and chars[left] not in vowels:
            left += 1

        # move right to the previous vowel
        while left < right and chars[right] not in vowels:
            right -= 1

        # swap the two vowels
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverseVowels("hello"))     # Expected: holle
    print(reverseVowels("leetcode"))  # Expected: leotcede

'''
Pattern
Opposite Ends Two Pointers — both pointers hunt inward for vowels, swap them,
and continue. Non-vowels are skipped without moving.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (output char list; O(1) extra if mutated in place)

Better Possible?
No — a single inward pass is optimal.
'''
