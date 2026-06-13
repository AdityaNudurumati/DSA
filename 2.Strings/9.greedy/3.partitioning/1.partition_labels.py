'''
1. Partition Labels (Medium)
Problem Statement

Given a string s, partition it into as many parts as possible so that each
letter appears in at most one part.

Return a list of the sizes of these parts.

Example
Input:  s = "ababcbacadefegdehijhklij"
Output: [9, 7, 8]

Input:  s = "eccbbbbdec"
Output: [10]
'''


def partitionLabels(s):
    last = {ch: i for i, ch in enumerate(s)}  # last index of each char
    result = []
    start = 0   # start index of current partition
    end = 0     # farthest last-index seen so far in this partition

    for i, ch in enumerate(s):
        # Greedy: a partition must reach the last occurrence of every char in it.
        end = max(end, last[ch])
        # When the scan index meets that farthest boundary, cut here.
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


if __name__ == "__main__":
    print(partitionLabels("ababcbacadefegdehijhklij"))  # Expected: [9, 7, 8]
    print(partitionLabels("eccbbbbdec"))                # Expected: [10]


'''
Pattern
✅ Greedy Boundary Extension
Record each char's last index; sweep left to right extending the partition end
to the farthest last index, and cut when the scan reaches that end.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
(O(1) extra: last-index map bounded by 26 letters)
Better Possible?
❌ No. Two linear passes over the string; O(n) is optimal.
'''
