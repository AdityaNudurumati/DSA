'''
1. Implement Stack using Queues (Easy)
Problem Statement

Implement a LIFO stack using only queue operations. Support:
- push(x):  add x on top
- pop():    remove and return the top element
- top():    return the top element without removing it
- empty():  return True if the stack has no elements

A queue is FIFO (enqueue at back, dequeue from front). We must mimic LIFO using it.

Example
Input:
push 1; push 2; top; pop; empty

Output:
top   -> 2
pop   -> 2
empty -> False
'''

from collections import deque


class MyStack:

    def __init__(self):
        self._q = deque()                  # single FIFO queue

    def push(self, x):
        # Enqueue, then rotate every earlier element behind x so x sits at the
        # front. After this the queue's front is always the stack's top. O(n).
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        return self._q.popleft()           # front is the top -> O(1)

    def top(self):
        if self.empty():
            raise IndexError("top from empty stack")
        return self._q[0]                  # peek the front (the top)

    def empty(self):
        return not self._q


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())        # Expected: 2
    print(s.pop())        # Expected: 2
    print(s.empty())      # Expected: False

'''
Pattern
✅ Design — Stack using a single Queue (rotate-on-push)

Key Observation
A queue only exposes its front, but a stack needs its most-recent element first.
By rotating the queue after each push (move all older items behind the new one),
the newest element is always at the front, so pop/top become O(1).

| Metric | Value          |
| ------ | -------------- |
| Time   | push O(n), pop/top/empty O(1) |
| Space  | O(n)           |

Better Possible?
❌ Not asymptotically — one operation must be O(n) (push here, or pop in the
   pop-costly two-queue variant); total work per element is still bounded.
'''
