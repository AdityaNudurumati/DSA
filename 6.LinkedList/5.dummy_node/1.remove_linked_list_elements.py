'''
203. Remove Linked List Elements (Easy)
Problem Statement

Given the head of a linked list and an integer val, remove all the nodes of the
linked list that have Node.val == val, and return the new head.

Because nodes equal to val may sit at the very front (and several may be
consecutive), a dummy head lets us treat the head exactly like any other node.

Example:
Input:  head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''


# --- minimal singly linked list + helpers ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):            # list -> head
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):            # head -> list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# --- solution ---
def removeElements(head, val):
    dummy = ListNode(0, head)      # dummy in front so head deletions are uniform
    prev = dummy
    while prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next   # unlink the matching node
        else:
            prev = prev.next             # keep, advance
    return dummy.next


if __name__ == "__main__":
    print(to_list(removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)))  # Expected: [1, 2, 3, 4, 5]
    print(to_list(removeElements(build([7, 7, 7, 7]), 7)))           # Expected: []


'''
Pattern
✅ Dummy Node
A dummy head sits before the real head, so removing a matching head node is the
same operation as removing any interior node (prev.next = prev.next.next). No
special-casing the front, single clean pass with one pointer.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Every node must be inspected once to decide removal; O(n) time is optimal
and the dummy keeps space at O(1).
'''
