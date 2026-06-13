'''
206. Reverse Linked List (Easy)
Problem Statement

Given the head of a singly linked list, reverse the list and return the
new head.

Input:
head = [1,2,3,4,5]

Output:
[5,4,3,2,1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):           # list -> linked list
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):           # linked list -> list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next      # remember rest of list
        curr.next = prev     # flip the pointer backwards
        prev = curr          # advance prev
        curr = nxt           # advance curr
    return prev              # prev is the new head


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    print(to_list(reverseList(head)))  # Expected: [5, 4, 3, 2, 1]


'''
Pattern
✅ Reversal (iterative pointer flip)
Walk once keeping prev/curr/nxt; re-point each node to its predecessor.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Better Possible?
❌ No
Every node's pointer must be touched once; O(n) time is optimal and the
iterative version is already O(1) space (recursion would cost O(n) stack).
'''
