'''
19. Remove Nth Node From End of List (Medium)
Problem Statement

Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Input:
head = [1,2,3,4,5], n = 2

Output:
[1,2,3,5]

Explanation:
The 2nd node from the end (value 4) is removed.
For head = [1], n = 1 the only node is removed, leaving [].
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


def removeNthFromEnd(head, n):
    # Dummy node handles removal of the head uniformly.
    # Advance fast n steps ahead, then move fast & slow together; when fast hits
    # the end, slow sits just before the node to delete.
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next   # unlink the nth-from-end node
    return dummy.next


if __name__ == "__main__":
    print(to_list(removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))  # Expected: [1, 2, 3, 5]
    print(to_list(removeNthFromEnd(build([1]), 1)))              # Expected: []


'''
Pattern
✅ Nth Node From End (two pointers n apart) + Dummy Node
Keeping fast exactly n nodes ahead of slow means slow stops one before the target in
a single pass. The dummy node removes the special case where the head itself is deleted.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
A two-pass length-count solution is also O(n)/O(1); this one-pass gap approach is
already optimal. Every node may need visiting once.
'''
