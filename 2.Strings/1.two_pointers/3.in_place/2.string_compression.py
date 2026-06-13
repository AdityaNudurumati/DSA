'''
2. String Compression (Medium)
Problem Statement

Given an array of characters chars, compress it in-place. For each group of
consecutive repeating characters:

If the group length is 1, append just the character.
Otherwise, append the character followed by the group length (as digits).

The compressed result must be written into the beginning of chars. Return the
new length k; the first k characters hold the answer.

Example
Input:
chars = ["a","a","b","b","c","c","c"]

Output:
6, and chars starts with ["a","2","b","2","c","3"]
'''

def compress(chars):

    write = 0   # slow pointer: where to write next
    read = 0    # fast pointer: scans groups
    n = len(chars)

    while read < n:
        ch = chars[read]
        count = 0

        # count this run of identical characters
        while read < n and chars[read] == ch:
            read += 1
            count += 1

        # write the character
        chars[write] = ch
        write += 1

        # write the count digits only when count > 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    k = compress(chars)
    print(k)            # Expected: 6
    print(chars[:k])    # Expected: ['a', '2', 'b', '2', 'c', '3']

'''
Pattern
In-place Processing (slow/fast pointers) — the fast pointer measures each run,
the slow pointer writes the character plus its count back into the same array.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No — every character is read once and written at most a constant amount.
'''
