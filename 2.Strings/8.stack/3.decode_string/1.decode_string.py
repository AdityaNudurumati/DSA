'''
1. Decode String (Medium)
Problem Statement

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is repeated exactly k times. k is a positive integer. The input is always
valid; there are no extra spaces and digits only appear as repeat counts.

Example
Input:
s = "3[a2[c]]"

Output:
"accaccacc"
'''

def decodeString(s):

    stack = []          # holds (string_built_so_far, repeat_count) on each '['
    cur = ''            # current segment being built
    num = 0             # current repeat count being parsed

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)          # build multi-digit counts
        elif c == '[':
            stack.append((cur, num))         # save context, then reset
            cur = ''
            num = 0
        elif c == ']':
            prev, count = stack.pop()        # restore outer context
            cur = prev + cur * count         # repeat this segment, attach
        else:
            cur += c                         # ordinary letter

    return cur


if __name__ == "__main__":
    print(decodeString("3[a]2[bc]"))      # Expected: aaabcbc
    print(decodeString("3[a2[c]]"))       # Expected: accaccacc
    print(decodeString("2[abc]3[cd]ef"))  # Expected: abcabccdcdcdef

'''
Pattern
✅ Stack (save outer context on '[', resolve on ']')
Push (built-string, count) when entering a bracket; on ']' pop and multiply,
which naturally handles arbitrary nesting.

| Metric | Value |
| ------ | ----- |
| Time   | O(n_out)  |
| Space  | O(n_out)  |

Better Possible?
❌ No. Output must be produced; work is proportional to the decoded length.
'''
