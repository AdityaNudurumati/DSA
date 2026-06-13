'''
23. Merge k Sorted Lists (Hard)
Problem Statement

You are given an array of k linked lists lists, each linked list is sorted in
ascending order. Merge all the linked lists into one sorted linked list and
return its head.

Example
Input:
lists = [[1,4,5],[1,3,4],[2,6]]

Output:
[1,1,2,3,4,4,5,6]
'''

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def build(values):                       # list -> linked list
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next

def to_list(head):                       # linked list -> list
    out = []
    while head:
        out.append(head.val); head = head.next
    return out


def mergeKLists(lists):
    # Min-heap of the current front node of each list.
    # Tie-break on a counter `idx` so two equal values never compare ListNodes
    # (ListNode has no __lt__), keeping the heap stable and crash-free.
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = tail = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)   # smallest front overall
        tail.next = node; tail = node        # splice it onto the result
        if node.next:                        # refill from the same list
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


if __name__ == "__main__":
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print(to_list(mergeKLists(lists)))
    # Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_list(mergeKLists([])))                       # Expected: []
    print(to_list(mergeKLists([build([]), build([1])])))  # Expected: [1]

'''
Pattern
✅ Min-heap of the k list heads (k-way merge)

Key Observation
The next smallest node overall is always one of the k current front nodes. A heap
of size k pops that minimum in O(log k); after popping, push the popped node's
successor so the heap always holds at most one node per list. The (val, idx, node)
tuple uses idx as a tie-breaker so equal values never force a ListNode comparison.

| Metric | Value        |
| ------ | ------------ |
| Time   | O(N log k)   | (N = total nodes across all lists)
| Space  | O(k)         | (heap holds one node per list)

Better Possible?
❌ No. Pairwise/divide-and-conquer merging is also O(N log k); the heap matches the
lower bound with O(k) auxiliary space.
'''
