'''
1. Maximum Frequency Stack (Hard)
Problem Statement

Design a stack-like data structure to push elements and pop the most frequent
element from the stack.

Implement the FreqStack class:
- push(val) pushes val onto the stack.
- pop() removes and returns the most frequent element in the stack. If there is a
  tie for the most frequent element, the element closest to the top of the stack
  is removed and returned.

Example
Input:
push(5); push(7); push(5); push(7); push(4); push(5); pop(); pop(); pop(); pop()

Output:
5, 7, 5, 4
'''

from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)          # val -> current count
        self.groups = defaultdict(list)       # frequency level -> stack of vals
        self.maxfreq = 0

    def push(self, val):
        # Increment this value's frequency and place it on its new frequency level.
        self.freq[val] += 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)
        self.groups[f].append(val)            # stack ordering breaks ties by recency

    def pop(self):
        # Take from the highest frequency level; its top is the most recent such val.
        val = self.groups[self.maxfreq].pop()
        self.freq[val] -= 1
        # If the top frequency level is now empty, drop to the next level down.
        if not self.groups[self.maxfreq]:
            self.maxfreq -= 1
        return val


if __name__ == "__main__":
    st = FreqStack()
    for x in (5, 7, 5, 7, 4, 5):
        st.push(x)
    print(st.pop())   # Expected: 5
    print(st.pop())   # Expected: 7
    print(st.pop())   # Expected: 5
    print(st.pop())   # Expected: 4

'''
Pattern
✅ Min / Max Stack (frequency buckets, one stack per frequency level)
Group values by how many times they currently appear; a per-level stack keeps the
most recent value of that frequency on top, so popping the top of the highest
non-empty level returns the most frequent and breaks ties by recency.

| Metric | Value |
| ------ | ----- |
| Time   | O(1)  |
| Space  | O(n)  |

Better Possible?
❌ No. O(1) push/pop is optimal; storing all elements requires O(n) space.
'''
