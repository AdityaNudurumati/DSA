'''
2. Longest Common Prefix (Easy)
Problem Statement

Write a function to find the longest common prefix string shared by all strings
in an array. If there is no common prefix, return an empty string "".

Example
Input:
["flower","flow","flight"]

Output:
"fl"
'''

def longestCommonPrefix(strs):

    if not strs:
        return ""

    # Build a trie, then walk down while every node has exactly ONE child and is
    # not the end of a word. That single chain IS the common prefix.
    root = {}
    for word in strs:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True  # mark word end so a full short word stops the prefix

    prefix = []
    node = root
    while True:
        # stop if a word ended here, or the path branches into multiple children
        if '#' in node:
            break
        children = [k for k in node if k != '#']
        if len(children) != 1:
            break
        ch = children[0]
        prefix.append(ch)
        node = node[ch]

    return "".join(prefix)


if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))  # Expected: fl
    print(longestCommonPrefix(["dog", "racecar", "car"]))     # Expected:

'''
Pattern
✅ Trie / Prefix Search — the common prefix is the longest single-child chain from
   the root before the words diverge or one word ends.

| Metric | Value                               |
| ------ | ----------------------------------- |
| Time   | O(S) where S = sum of all char count |
| Space  | O(S) for the trie                   |

Better Possible?
Vertical scanning (compare column by column) solves it in O(S) time with O(1)
extra space and no trie, so for THIS single query that is leaner. The trie shines
when many prefix queries reuse the same word set.
'''
