'''
2. Design a Priority Queue (Medium)
Problem Statement

Implement a MIN priority queue FROM SCRATCH using an array-backed binary heap
(no use of the heapq library for the core operations). Support:
- push(val) : insert a value.
- pop()     : remove and return the smallest value.
- peek()    : return the smallest value without removing it.
- size()    : number of elements currently stored.

The smallest element must always sit at the root (index 0). Use sift-up after a
push and sift-down after a pop to restore the heap property.

Example:
Input:
push(5); push(3); push(8); push(1); pop(); pop(); peek(); size()
Output:
1
3
5
2
'''

import heapq  # imported per convention; the PQ below is hand-rolled, not using it


class MinPriorityQueue:
    def __init__(self):
        self.heap = []  # array-backed complete binary tree

    def size(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]  # root is always the minimum

    def push(self, val):
        # append at the end, then bubble it up to its correct level
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        n = len(self.heap)
        # swap root with last element, drop the old root, sift the new root down
        self.heap[0], self.heap[n - 1] = self.heap[n - 1], self.heap[0]
        smallest = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return smallest

    def _sift_up(self, i):
        # move element up while it is smaller than its parent
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


if __name__ == "__main__":
    pq = MinPriorityQueue()
    pq.push(5)
    pq.push(3)
    pq.push(8)
    pq.push(1)
    print(pq.pop())   # Expected: 1
    print(pq.pop())   # Expected: 3
    print(pq.peek())  # Expected: 5
    print(pq.size())  # Expected: 2


'''
Pattern
✅ Design — Binary Heap (array-backed)
A complete binary tree is stored in a flat array where node i has children at
2i+1 and 2i+2 and parent at (i-1)//2. push appends then sift-ups; pop swaps the
root with the last leaf, removes it, then sift-downs. This is exactly what the
heapq library does internally, built here by hand.

| Metric | Value     |
| ------ | --------- |
| Time   | push/pop O(log n), peek/size O(1) |
| Space  | O(n)      |

Better Possible?
❌ Not for a comparison-based PQ — log n per push/pop is optimal for a binary
heap. Specialized structures (Fibonacci heap) improve amortized push to O(1) but
add large constants and complexity, so a binary heap is the practical choice.
'''
