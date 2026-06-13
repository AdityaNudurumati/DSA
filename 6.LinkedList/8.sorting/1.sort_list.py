'''
148. Sort List (Medium)
Problem Statement

Given the head of a linked list, return the list after sorting it in
ascending order.

You must sort in O(n log n) time, which rules out insertion sort and points
straight at merge sort (it splits and merges without needing random access).

Example:
Input:  head = [4,2,1,3]
Output: [1,2,3,4]

Input:  head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Input:  head = []
Output: []
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):           # list -> head
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):           # head -> list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def merge(a, b):
    # merge two sorted lists into one sorted list
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b       # attach the remaining tail
    return dummy.next


def sortList(head):
    # base case: 0 or 1 node is already sorted
    if not head or not head.next:
        return head

    # split at the middle using slow/fast (fast starts ahead so left half
    # is never empty for a 2-node list)
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None     # cut the list in two halves

    # recurse on each half, then merge the sorted halves
    return merge(sortList(head), sortList(mid))


if __name__ == "__main__":
    print(to_list(sortList(build([4, 2, 1, 3]))))      # Expected: [1, 2, 3, 4]
    print(to_list(sortList(build([-1, 5, 3, 4, 0]))))  # Expected: [-1, 0, 3, 4, 5]
    print(to_list(sortList(build([])))) 	           # Expected: []


'''
Pattern
✅ Merge Sort on a Linked List
Find the middle with slow/fast pointers, recursively sort each half, then merge
the two sorted halves. Merge sort suits linked lists because splitting and
merging only need sequential access and pointer rewiring (no shifting).

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(log n)   |

Space is O(log n) from the recursion stack. Better Possible?
❌ Not asymptotically — O(n log n) is the comparison-sort lower bound.
A bottom-up iterative merge sort reaches O(1) extra space but the same time.
'''
