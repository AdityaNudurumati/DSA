'''
1. Min Stack (Medium)
Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:
- push(val) pushes val onto the stack.
- pop() removes the element on top of the stack.
- top() gets the top element.
- getMin() retrieves the minimum element in the stack.

All operations must run in O(1) time.

Example
Input:
push(-2); push(0); push(-3); getMin(); pop(); top(); getMin()

Output:
-3, 0, -2
'''

class MinStack:

    def __init__(self):
        # Each entry stores (value, min_so_far) so the running minimum
        # is always available in O(1) at the top of the stack.
        self.stack = []

    def push(self, val):
        # New minimum is val itself or the previous running minimum.
        m = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, m))

    def pop(self):
        # Discard the top; its paired minimum leaves with it.
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]          # current top value

    def getMin(self):
        return self.stack[-1][1]          # running minimum at the top


if __name__ == "__main__":
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    print(st.getMin())   # Expected: -3
    st.pop()
    print(st.top())      # Expected: 0
    print(st.getMin())   # Expected: -2

'''
Pattern
✅ Min / Max Stack (main stack + per-element running minimum)
Pairing each value with the minimum-so-far lets getMin read the top in O(1),
and the minimum is restored automatically on pop since it travels with its value.

| Metric | Value |
| ------ | ----- |
| Time   | O(1)  |
| Space  | O(n)  |

Better Possible?
❌ No. O(1) per operation is optimal; O(n) space is inherent to storing the elements.
'''
