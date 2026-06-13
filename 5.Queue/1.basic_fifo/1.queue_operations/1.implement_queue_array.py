'''
1. Implement Queue using Array (Easy)
Problem Statement

Implement a FIFO queue backed by a Python list (dynamic array).

Support the operations:
- enqueue(x) : add x to the rear of the queue
- dequeue()  : remove and return the item at the front
- peek()     : return the front item without removing it
- size()     : number of items currently in the queue
- is_empty()  : True if the queue has no items

Input:
enqueue 1, enqueue 2, enqueue 3
dequeue, peek, size

Output:
dequeue -> 1
peek    -> 2
size    -> 2
'''

class ArrayQueue:
    def __init__(self):
        self.data = []  # list acts as the backing array; front is index 0

    def enqueue(self, x):
        # append adds to the rear (end of list) in amortized O(1)
        self.data.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        # pop(0) removes the front; O(n) because elements shift left
        return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.data[0]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Expected: 1
    print(q.peek())     # Expected: 2
    print(q.size())     # Expected: 2


'''
Pattern
✅ Basic FIFO — Queue Operations
A list models the queue: append() pushes to the rear, pop(0) pops the front,
so removal order matches insertion order (first-in, first-out).

| Metric        | Value |
| ------------- | ----- |
| Time enqueue  | O(1)* |
| Time dequeue  | O(n)  |
| Time peek/size| O(1)  |
| Space         | O(n)  |
(* amortized for append)

Better Possible?
✅ Yes. dequeue is O(n) here because pop(0) shifts every element. Using
collections.deque (or a linked list with a tail pointer, see next file) makes
dequeue O(1). The array version is shown to expose the cost of front removal.
'''
