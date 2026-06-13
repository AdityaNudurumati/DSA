'''
1670. Design Front Middle Back Queue (Medium)
Problem Statement

Design a queue that supports push and pop operations at the front, middle, and back.

Implement the FrontMiddleBackQueue class:
  FrontMiddleBackQueue()  initializes the queue.
  void pushFront(val)     adds val to the front.
  void pushMiddle(val)    adds val to the middle.
  void pushBack(val)      adds val to the back.
  int popFront()          removes and returns the front element, or -1 if empty.
  int popMiddle()         removes and returns the middle element, or -1 if empty.
  int popBack()           removes and returns the back element, or -1 if empty.

When there are two middle positions, the operations favor the FRONT one:
  - pushMiddle of size-6 queue [1,2,3,4,5,6] inserts at index 3 -> [1,2,3,val,4,5,6]
  - popMiddle of [1,2,3,4,5,6] removes index 2 (value 3).

Example
Input:
pushFront(1); pushBack(2); pushMiddle(3); pushMiddle(4)   # queue is [1,4,3,2]
popFront(); popMiddle(); popMiddle(); popBack(); popFront()

Output:
1, 3, 4, 2, -1
'''

from collections import deque


class FrontMiddleBackQueue:
    # Two deques: `left` holds the front half, `right` holds the back half.
    # Invariant kept after every op: len(left) <= len(right) <= len(left) + 1.
    # The true middle for pushMiddle is right[0]; for popMiddle it is left[-1]
    # when the sizes are equal, otherwise right[0]. The balance() helper restores
    # the invariant so the middle is always reachable in O(1).
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # Restore: left no longer than right, right at most one longer than left.
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val):
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val):
        # Favor the front middle: when total is even, the new value becomes the
        # tail of `left`; otherwise it becomes the head of `right`.
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)
        self._balance()

    def pushBack(self, val):
        self.right.append(val)
        self._balance()

    def popFront(self):
        if not self.right:                  # empty (right is never shorter than left)
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self._balance()
        return val

    def popMiddle(self):
        if not self.right:
            return -1
        # Front-favored middle: equal sizes -> take from left's tail, else right's head.
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popBack(self):
        if not self.right:
            return -1
        val = self.right.pop()
        self._balance()
        return val


if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushBack(2)
    q.pushMiddle(3)
    q.pushMiddle(4)               # queue is now [1, 4, 3, 2]
    print(q.popFront())           # Expected: 1
    print(q.popMiddle())          # Expected: 3
    print(q.popMiddle())          # Expected: 4
    print(q.popBack())            # Expected: 2
    print(q.popFront())           # Expected: -1

'''
Pattern
✅ Double Ended Queue — two balanced deques split at the middle

Technique & why
Splitting the sequence into a `left` and `right` deque, with the invariant
len(left) <= len(right) <= len(left)+1, keeps the middle element at the boundary
(left's tail / right's head). Every push/pop touches an end of one deque and then
a single rebalance move, so all six operations are O(1). A single deque cannot
reach the middle in O(1); two deques make the middle a "front/back" of its half.

| Metric | Value |
| ------ | ----- |
| Time   | O(1)  | (per operation, amortized & worst case — one balance move)
| Space  | O(n)  |

Better Possible?
❌ No. O(1) per operation is optimal; you cannot beat constant time.
'''
