'''
143. Reorder List (Medium)
Problem Statement

You are given the head of a singly linked list:
    L0 -> L1 -> ... -> Ln-1 -> Ln
Reorder it in-place to:
    L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the node values; only the node pointers may change.

Example:
Input:  head = [1,2,3,4]
Output: [1,4,2,3]

Input:  head = [1,2,3,4,5]
Output: [1,5,2,4,3]
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


def reorderList(head):
    if not head or not head.next:
        return head

    # 1) find middle (slow ends at end of first half for even/odd lengths)
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2) reverse the second half (everything after slow)
    second = slow.next
    slow.next = None           # cut the list into two halves
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev              # head of the reversed second half

    # 3) merge the two halves alternately
    first = head
    while second:
        f_next, s_next = first.next, second.next
        first.next = second
        second.next = f_next
        first, second = f_next, s_next

    return head


if __name__ == "__main__":
    print(to_list(reorderList(build([1, 2, 3, 4]))))     # Expected: [1, 4, 2, 3]
    print(to_list(reorderList(build([1, 2, 3, 4, 5]))))  # Expected: [1, 5, 2, 4, 3]


'''
Pattern
✅ List Rearrangement (find-middle + reverse + merge)
Classic three-step recipe: split with fast-slow pointers, reverse the second
half in place, then zip the two halves together. Each step is O(1) space.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
A value/array copy would also be O(n) time but cost O(n) space; this pointer
approach is already optimal in both.
'''
