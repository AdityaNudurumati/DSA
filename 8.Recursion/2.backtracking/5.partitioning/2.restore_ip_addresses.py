'''
93. Restore IP Addresses (Medium)
Problem Statement

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You cannot reorder or remove digits.

Example:
Input:
s = "25525511135"

Output:
["255.255.11.135", "255.255.111.35"]
'''


def restoreIpAddresses(s):
    result = []

    def valid(seg):
        # no leading zeros (unless "0"), and within 0..255
        if len(seg) > 1 and seg[0] == "0":
            return False
        return 0 <= int(seg) <= 255

    def backtrack(start, parts):
        if len(parts) == 4:               # placed all four octets
            if start == len(s):           # and used every digit
                result.append(".".join(parts))
            return
        # an octet is 1 to 3 digits
        for length in range(1, 4):
            if start + length > len(s):
                break
            seg = s[start:start + length]
            if valid(seg):
                parts.append(seg)
                backtrack(start + length, parts)
                parts.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    s = "25525511135"
    print(sorted(restoreIpAddresses(s)))
    # Expected: ['255.255.11.135', '255.255.111.35']


'''
Pattern
✅ Partitioning via Backtracking with constraints
We cut the string into 4 segments, trying lengths 1..3 and only recursing when
the segment is a legal octet; valid endings require all digits consumed.
| Metric | Value  |
| ------ | ------ |
| Time   | O(1)   |
| Space  | O(1)   |
Better Possible?
❌ No

There are at most 3^3 dot placements and a fixed 4 octets, so the work is
bounded by a constant regardless of input length.
'''
