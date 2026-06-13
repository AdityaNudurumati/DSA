'''
2. Implement Queue using Linked List (Easy)
Problem Statement

Implement a FIFO queue backed by a singly linked list with both a head pointer
(front, for dequeue/peek) and a tail pointer (rear, for enqueue), so every
operation runs in O(1).

Support the operations:
- enqueue(x) : add x to the rear (append after tail)
- dequeue()  : remove and return the item at the front (head)
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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None  # front: where we dequeue/peek
        self.tail = None  # rear: where we enqueue
        self.count = 0

    def enqueue(self, x):
        node = Node(x)
        if self.tail is None:
            # empty queue: new node is both head and tail
            self.head = self.tail = node
        else:
            # link new node after current tail, then advance tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        node = self.head
        self.head = self.head.next  # advance front
        if self.head is None:        # queue became empty -> reset tail too
            self.tail = None
        self.count -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.head.value

    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None


if __name__ == "__main__":
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Expected: 1
    print(q.peek())     # Expected: 2
    print(q.size())     # Expected: 2


'''
Pattern
✅ Basic FIFO — Queue Operations
A singly linked list with head + tail pointers. enqueue links after tail,
dequeue pops from head; keeping both ends as pointers makes every op O(1)
without any element shifting.

| Metric         | Value |
| -------------- | ----- |
| Time enqueue   | O(1)  |
| Time dequeue   | O(1)  |
| Time peek/size | O(1)  |
| Space          | O(n)  |

Better Possible?
❌ No on time — all operations are already O(1). This fixes the O(n) dequeue of
the array version. In practice collections.deque gives the same O(1) ends with
less per-node overhead, but the linked list shows the underlying mechanism.
'''
