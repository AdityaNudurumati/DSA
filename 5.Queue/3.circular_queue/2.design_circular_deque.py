'''
2. Design Circular Deque (Medium)
Problem Statement

Design your implementation of the circular double-ended queue (deque) (LC641).
Implement the MyCircularDeque class:
  MyCircularDeque(k)   initialize the deque with fixed capacity k
  insertFront(value)   add an item at the front; return True if successful
  insertLast(value)    add an item at the rear;  return True if successful
  deleteFront()        delete an item from the front; return True if successful
  deleteLast()         delete an item from the rear;  return True if successful
  getFront()           get the front item; return -1 if empty
  getRear()            get the last item;  return -1 if empty
  isEmpty()            check whether the deque is empty
  isFull()             check whether the deque is full

Example:
Input (capacity 3):
  insertLast(1), insertLast(2), insertFront(3), insertFront(4), getRear(),
  isFull(), deleteLast(), insertFront(4), getFront()
Output:
  True, True, True, False, 2, True, True, True, 4
'''

class MyCircularDeque:
    def __init__(self, k):
        self.capacity = k
        self.data = [0] * k       # fixed-size ring buffer
        self.front = 0            # index of the current front element
        self.size = 0             # number of elements currently stored

    def insertFront(self, value):
        if self.isFull():
            return False
        # move front one slot backwards around the ring, then write
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        # simply drop the last element by shrinking size
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        rear = (self.front + self.size - 1) % self.capacity
        return self.data[rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    dq = MyCircularDeque(3)
    print(dq.insertLast(1))    # Expected: True
    print(dq.insertLast(2))    # Expected: True
    print(dq.insertFront(3))   # Expected: True
    print(dq.insertFront(4))   # Expected: False
    print(dq.getRear())        # Expected: 2
    print(dq.isFull())         # Expected: True
    print(dq.deleteLast())     # Expected: True
    print(dq.insertFront(4))   # Expected: True
    print(dq.getFront())       # Expected: 4


'''
Pattern
Circular Deque (double-ended ring buffer): a fixed array with a front index and a
size counter. insertLast writes at (front + size) % capacity; insertFront moves the
front pointer one slot backwards modulo capacity and writes there. Both deletions
just adjust front/size. All operations are O(1) with no shifting, and the size
counter disambiguates empty (size == 0) from full (size == capacity).

| Metric | Value |
| ------ | ----- |
| Time   | O(1) per operation |
| Space  | O(k)  |

Better Possible?
No. Every operation is O(1) and O(k) storage is required to hold up to k elements.
This is optimal.
'''
