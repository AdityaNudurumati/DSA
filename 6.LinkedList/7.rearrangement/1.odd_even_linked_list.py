'''
328. Odd Even Linked List (Medium)
Problem Statement

Given the head of a singly linked list, group all the nodes with ODD indices
together followed by the nodes with EVEN indices, and return the reordered list.

The first node is considered odd, the second node even, and so on. Indices refer
to node POSITION, not value. Relative order inside each group must be preserved.
Solve it in O(1) extra space and O(n) time.

Example:
Input:  head = [1,2,3,4,5]
Output: [1,3,5,2,4]
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


def oddEvenList(head):
    # Empty or single node: nothing to rearrange.
    if not head or not head.next:
        return head

    odd = head                 # tail of the odd chain (position 1,3,5,...)
    even = head.next           # tail of the even chain (position 2,4,6,...)
    even_head = even           # remember where the even chain begins

    while even and even.next:
        odd.next = even.next   # splice next odd node out
        odd = odd.next
        even.next = odd.next   # splice next even node out
        even = even.next

    odd.next = even_head       # attach even chain after the odd chain
    return head


if __name__ == "__main__":
    print(to_list(oddEvenList(build([1, 2, 3, 4, 5]))))  # Expected: [1, 3, 5, 2, 4]
    print(to_list(oddEvenList(build([2, 1, 3, 5, 6, 4, 7]))))  # Expected: [2, 3, 6, 7, 1, 5, 4]


'''
Pattern
✅ List Rearrangement (two-chain split by index parity)
Walk once, weaving each node into either the odd or even chain by its position,
then stitch the even chain onto the tail of the odd chain. No extra nodes built,
so it is in-place pointer surgery.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
Every node must be visited once and O(1) space is already optimal.
'''
