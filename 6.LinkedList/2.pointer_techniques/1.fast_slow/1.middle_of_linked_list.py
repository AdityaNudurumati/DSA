'''
876. Middle of the Linked List (Easy)
Problem Statement

Given the head of a singly linked list, return the middle node of the list.

If there are two middle nodes (even length), return the SECOND middle node.

Input:
head = [1,2,3,4,5]

Output:
3

Explanation:
The middle node has value 3.
For [1,2,3,4,5,6] there are two middles (3 and 4); we return the second -> 4.
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


def middleNode(head):
    # Fast-slow: fast moves 2x, slow 1x. When fast falls off the end,
    # slow sits on the middle. For even length this lands on the 2nd middle.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    print(middleNode(build([1, 2, 3, 4, 5])).val)        # Expected: 3
    print(middleNode(build([1, 2, 3, 4, 5, 6])).val)     # Expected: 4


'''
Pattern
✅ Fast-Slow Pointers
Advance fast twice as quickly as slow; the offset guarantees slow is centered
when fast runs out of nodes. One pass, no length pre-count, constant memory.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
Must touch the front half of the nodes at minimum; O(n) time, O(1) space is optimal.
'''
