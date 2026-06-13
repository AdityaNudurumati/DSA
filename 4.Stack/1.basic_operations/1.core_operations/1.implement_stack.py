'''
1. Implement Stack (Easy)
Problem Statement

Implement a LIFO stack backed by a Python list, supporting the core operations:
- push(x):   add x on top
- pop():     remove and return the top element
- peek():    return the top element without removing it
- is_empty(): return True if the stack has no elements
- size():    return the number of elements

Example
Input:
push 1; push 2; push 3; peek; pop; pop; is_empty

Output:
peek -> 3
pop  -> 3
pop  -> 2
is_empty -> False
'''

class Stack:

    def __init__(self):
        self._data = []            # list end is the top of the stack

    def push(self, x):
        self._data.append(x)       # O(1) amortized append at the end

    def pop(self):
        if self.is_empty():        # guard against popping an empty stack
            raise IndexError("pop from empty stack")
        return self._data.pop()    # remove and return the top (LIFO)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]      # top without removing

    def is_empty(self):
        return not self._data      # empty list is falsy

    def size(self):
        return len(self._data)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())       # Expected: 3
    print(s.pop())        # Expected: 3
    print(s.pop())        # Expected: 2
    print(s.is_empty())   # Expected: False

'''
Pattern
✅ Basic Stack — list-backed LIFO

Key Observation
A Python list already gives O(1) amortized push (append) and pop from its end, so
the list's tail is the natural "top" of the stack; every operation maps directly.

| Metric | Value |
| ------ | ----- |
| Time   | O(1)  |
| Space  | O(n)  |

Better Possible?
❌ No — all operations are already O(1).
'''
