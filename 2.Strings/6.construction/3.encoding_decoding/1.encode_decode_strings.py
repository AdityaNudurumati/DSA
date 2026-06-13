'''
1. Encode and Decode Strings (Medium)
Problem Statement

Design an algorithm to encode a list of strings into a single string. The
encoded string is then sent over the network and decoded back into the
original list of strings.

The strings may contain any of the 256 ASCII characters (including digits,
'#', and spaces), so the scheme must be unambiguous.

Example
Input:
strs = ["lint", "code", "love", "you"]

Output (round-trip):
["lint", "code", "love", "you"]
'''

def encode(strs):
    # length-prefix scheme: "<len>#<word>" for each string.
    # The '#' separates the (always-numeric) length from the word, and the
    # length tells the decoder exactly how many chars to read -> unambiguous
    # even if a word itself contains '#' or digits.
    parts = []
    for s in strs:
        parts.append(str(len(s)) + '#' + s)
    return ''.join(parts)


def decode(s):
    res = []
    i = 0
    while i < len(s):
        # read digits up to the '#' delimiter to get the length
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        # the word is exactly 'length' chars after the '#'
        word = s[j + 1: j + 1 + length]
        res.append(word)
        i = j + 1 + length
    return res


if __name__ == "__main__":
    original = ["lint", "code", "love", "you"]
    round_trip = decode(encode(original))
    print(round_trip)                    # Expected: ['lint', 'code', 'love', 'you']
    print(round_trip == original)        # Expected: True


'''
Pattern
✅ Encoding/Decoding (length-prefix framing)
Prefix each string with its length and a delimiter ("4#word"). The numeric
length makes decoding deterministic regardless of the word's contents.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(N) total chars     |
| Space  | O(N)                 |

Better Possible?
❌ No — every character must be written and read once.
'''
