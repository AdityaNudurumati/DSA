'''
2. Remove All Adjacent Duplicates In String II (Medium)
Problem Statement

You are given a string s and an integer k. A k-duplicate removal consists of
choosing k adjacent and equal letters from s and removing them.

Repeatedly make k-duplicate removals on s until no more can be made, then return the
final string. The answer is guaranteed to be unique.

Example
Input:
s = "deeedbbcccbdaa", k = 3

Output:
"aa"

Explanation:
remove "eee" -> "ddbbcccbdaa", remove "ccc" -> "ddbbbdaa", remove "bbb" ->
"dddaa", remove "ddd" -> "aa".
'''

def removeDuplicates(s, k):

    stack = []                       # each entry: [char, current_run_count]

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1        # extend the run of the same char
            if stack[-1][1] == k:
                stack.pop()          # run hit k: remove the whole group
        else:
            stack.append([c, 1])     # new char, run starts at 1

    # rebuild: each surviving entry contributes char * count
    return ''.join(char * count for char, count in stack)


if __name__ == "__main__":
    print(removeDuplicates("deeedbbcccbdaa", 3))        # Expected: aa
    print(removeDuplicates("pbbcggttciiippooaais", 2))  # Expected: ps

'''
Pattern
✅ Stack with counts (collapse runs of length k)
Store (char, count) pairs so equal neighbors merge; pop when a run reaches k.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |

Better Possible?
❌ No. Single pass; each char processed once.
'''
