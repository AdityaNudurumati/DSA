'''
1. Implement Queue using Stacks (Easy)
Problem Statement

Implement a FIFO queue using only stack operations. Support:
- push(x):  add x at the back
- pop():    remove and return the front element
- peek():   return the front element without removing it
- empty():  return True if the queue has no elements

A stack is LIFO (push/pop at the top). Use two stacks to get FIFO with
amortized O(1) per operation.

Example
Input:
push 1; push 2; peek; pop; empty

Output:
peek  -> 1
pop   -> 1
empty -> False
'''


class MyQueue:

    def __init__(self):
        self._in = []                      # incoming pushes land here
        self._out = []                      # reversed order -> front on top

    def _transfer(self):
        # Move everything from in -> out only when out is empty. This reverses
        # the order so the oldest element ends up on top of out. Each element is
        # moved at most once, giving amortized O(1).
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def push(self, x):
        self._in.append(x)                 # O(1)

    def pop(self):
        self._transfer()
        if not self._out:
            raise IndexError("pop from empty queue")
        return self._out.pop()             # amortized O(1)

    def peek(self):
        self._transfer()
        if not self._out:
            raise IndexError("peek from empty queue")
        return self._out[-1]               # front sits on top of out

    def empty(self):
        return not self._in and not self._out


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())       # Expected: 1
    print(q.pop())        # Expected: 1
    print(q.empty())      # Expected: False

'''
Pattern
✅ Design — Queue using two Stacks (in / out, lazy transfer)

Key Observation
Reversing a stack once turns LIFO into FIFO. Keep an "in" stack for pushes and an
"out" stack for pops; only refill "out" (by draining "in") when it is empty. Each
element is pushed onto in once, moved to out once, and popped once -> amortized O(1).

| Metric | Value                          |
| ------ | ------------------------------ |
| Time   | push O(1); pop/peek amortized O(1) |
| Space  | O(n)                           |

Better Possible?
❌ No — amortized O(1) per operation is optimal for this construction.
'''
