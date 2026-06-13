'''
92. Reverse Linked List II (Medium)
Problem Statement

Given the head of a singly linked list and two integers left and right
where left <= right, reverse the nodes from position left to position
right (1-indexed) and return the list.

Input:
head = [1,2,3,4,5], left = 2, right = 4

Output:
[1,4,3,2,5]
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


def reverseBetween(head, left, right):
    dummy = ListNode(0, head)        # dummy handles left == 1 cleanly
    prev = dummy
    for _ in range(left - 1):        # walk to node just before `left`
        prev = prev.next

    curr = prev.next                 # first node of the sub-list to reverse
    # Head-insertion: repeatedly move the node after curr to the front.
    for _ in range(right - left):
        nxt = curr.next
        curr.next = nxt.next         # detach nxt
        nxt.next = prev.next         # nxt jumps to front of reversed part
        prev.next = nxt              # prev points to the new front
    return dummy.next


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    print(to_list(reverseBetween(head, 2, 4)))  # Expected: [1, 4, 3, 2, 5]


'''
Pattern
✅ Reversal (reverse a window via head-insertion)
Park `prev` before the window, then splice each following node to the
window's front. A dummy node removes the left == 1 edge case.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Better Possible?
❌ No
A single pass to reach `left` plus in-place relinking is optimal; the
sub-list nodes are each moved exactly once.
'''
