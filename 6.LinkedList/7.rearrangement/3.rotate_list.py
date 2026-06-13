'''
61. Rotate List (Medium)
Problem Statement

Given the head of a linked list, rotate the list to the RIGHT by k places.
Rotating right by 1 moves the last node to the front. k may be larger than the
list length, so reduce it modulo the length.

Example:
Input:  head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input:  head = [0,1,2], k = 4
Output: [2,0,1]
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


def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # 1) measure length and grab the tail
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    # 2) normalize k; if no net rotation, return as-is
    k %= length
    if k == 0:
        return head

    # 3) close into a ring, then cut after the new tail
    tail.next = head
    steps_to_new_tail = length - k     # node count before the break point
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


if __name__ == "__main__":
    print(to_list(rotateRight(build([1, 2, 3, 4, 5]), 2)))  # Expected: [4, 5, 1, 2, 3]
    print(to_list(rotateRight(build([0, 1, 2]), 4)))        # Expected: [2, 0, 1]


'''
Pattern
✅ List Rearrangement (make circular, then cut)
Connect the tail to the head to form a ring, reduce k modulo length, then walk to
the new tail (length - k % length nodes in) and break the ring there.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
We must traverse to find the length and the cut point; O(n)/O(1) is optimal.
'''
