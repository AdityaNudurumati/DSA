'''
1. Max Stack (Hard)
Problem Statement

Design a max stack data structure that supports the stack operations and also
supports finding and removing the stack's maximum element.

Implement the MaxStack class:
- push(x) pushes element x onto the stack.
- pop() removes the element on top of the stack and returns it.
- top() gets the element on top of the stack.
- peekMax() retrieves the maximum element in the stack.
- popMax() retrieves the maximum element and removes it. If there is more than one
  maximum, only remove the top-most one.

Example
Input:
push(5); push(1); push(5); top(); popMax(); top(); peekMax(); pop(); top()

Output:
5, 5, 1, 5, 1, 5
'''

class MaxStack:

    def __init__(self):
        # main: actual LIFO order.
        # maxes: running maximum so peekMax is O(1).
        self.main = []
        self.maxes = []

    def push(self, x):
        m = x if not self.maxes else max(x, self.maxes[-1])
        self.main.append(x)
        self.maxes.append(m)

    def pop(self):
        self.maxes.pop()
        return self.main.pop()

    def top(self):
        return self.main[-1]

    def peekMax(self):
        return self.maxes[-1]

    def popMax(self):
        m = self.maxes[-1]
        # Pop into a buffer until the top-most max is found, remove it,
        # then push the buffered values back (re-establishing running maxes).
        buffer = []
        while self.top() != m:
            buffer.append(self.pop())
        self.pop()                        # remove the maximum itself
        while buffer:
            self.push(buffer.pop())       # restore the elements above it
        return m


if __name__ == "__main__":
    st = MaxStack()
    st.push(5)
    st.push(1)
    st.push(5)
    print(st.top())       # Expected: 5
    print(st.popMax())    # Expected: 5
    print(st.top())       # Expected: 1
    print(st.peekMax())   # Expected: 5
    print(st.pop())       # Expected: 1
    print(st.top())       # Expected: 5

'''
Pattern
✅ Min / Max Stack (twin stack of running maxima + buffer for popMax)
peekMax/top/push/pop are O(1) via the running-max stack; popMax unwinds the
elements above the top-most maximum into a buffer, removes it, and replays them.

| Metric | Value |
| ------ | ----- |
| Time   | push/pop/top/peekMax O(1); popMax O(n) |
| Space  | O(n)  |

Better Possible?
✅ Yes. A balanced BST / two heaps with lazy deletion (or a doubly linked list +
TreeMap) can do popMax in O(log n), at the cost of more complex code.
'''
