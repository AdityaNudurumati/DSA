'''
1. Decode String (Medium)
Problem Statement

Given an encoded string, return its decoded form. The encoding rule is k[encoded_string],
where the encoded_string inside the brackets is repeated exactly k times. k is a positive
integer and the input is always valid (well-formed brackets, no stray digits).

Example
Input:
s = "3[a]2[bc]"

Output:
"aaabcbc"
'''

def decodeString(s):

    num_stack = []        # holds repeat counts waiting for their ']'
    str_stack = []        # holds the string built before each '['
    current = ""          # string being built at the current depth
    count = 0             # multi-digit number being parsed

    for ch in s:
        if ch.isdigit():
            count = count * 10 + int(ch)      # accumulate multi-digit k
        elif ch == "[":
            num_stack.append(count)           # save count for this context
            str_stack.append(current)         # save text built so far
            count = 0
            current = ""
        elif ch == "]":
            repeat = num_stack.pop()           # k for the closing bracket
            prev = str_stack.pop()             # text before the '['
            current = prev + current * repeat  # expand and reattach
        else:
            current += ch                      # ordinary letter

    return current


if __name__ == "__main__":
    print(decodeString("3[a]2[bc]"))      # Expected: aaabcbc
    print(decodeString("3[a2[c]]"))       # Expected: accaccacc
    print(decodeString("2[abc]3[cd]ef"))  # Expected: abcabccdcdcdef

'''
Pattern
✅ Stack Simulation — push (count, partial string) contexts; resolve on ']'

Key Observation
Each '[' opens a new nesting context, so we push the work-in-progress (the count and the
text built so far) and start fresh. On ']' we pop, repeat the inner text, and splice it
back into the outer context — naturally handling arbitrary nesting.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No — output length itself can be exponential in input, but the algorithm is optimal
relative to the decoded size.
'''
