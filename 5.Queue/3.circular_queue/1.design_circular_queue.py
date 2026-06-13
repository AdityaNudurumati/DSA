'''
1. Design Circular Queue (Medium)
Problem Statement

Design your implementation of the circular queue (LC622). The circular queue is a
linear data structure that follows FIFO and the last position is connected back to
the first to make a ring (a "ring buffer").

Implement the MyCircularQueue class:
  MyCircularQueue(k)   initialize the queue with fixed capacity k
  enQueue(value)       insert an element; return True if successful
  deQueue()            delete an element from the front; return True if successful
  Front()              get the front item; return -1 if empty
  Rear()               get the last item; return -1 if empty
  isEmpty()            check whether the queue is empty
  isFull()             check whether the queue is full

Example:
Input (capacity 3):
  enQueue(1), enQueue(2), enQueue(3), enQueue(4), Rear(),
  isFull(), deQueue(), enQueue(4), Rear()
Output:
  True, True, True, False, 3, True, True, True, 4
'''

class MyCircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.data = [0] * k       # fixed-size ring buffer
        self.front = 0            # index of the current front element
        self.size = 0             # number of elements currently stored

    def enQueue(self, value):
        if self.isFull():
            return False
        # rear index derived from front + size via modulo (no shifting)
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        # advance front around the ring
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.data[rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enQueue(1))   # Expected: True
    print(q.enQueue(2))   # Expected: True
    print(q.enQueue(3))   # Expected: True
    print(q.enQueue(4))   # Expected: False
    print(q.Rear())       # Expected: 3
    print(q.isFull())     # Expected: True
    print(q.deQueue())    # Expected: True
    print(q.enQueue(4))   # Expected: True
    print(q.Rear())       # Expected: 4


'''
Pattern
Circular Queue (ring buffer): a fixed array plus a front index and a size counter.
The rear position is computed as (front + size) % capacity, so enqueue/dequeue are
O(1) with no element shifting. Tracking size (instead of a separate rear pointer)
cleanly distinguishes the empty case (size == 0) from the full case
(size == capacity), avoiding the classic "ambiguous front == rear" problem.

| Metric | Value |
| ------ | ----- |
| Time   | O(1) per operation |
| Space  | O(k)  |

Better Possible?
No. Every operation is already O(1) time and the storage O(k) is required to hold
up to k elements. This is optimal.
'''
