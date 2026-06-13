'''
25. Reverse Nodes in k-Group (Hard)
Problem Statement

Given the head of a linked list, reverse the nodes of the list k at a
time and return the modified list. k is a positive integer <= the
list length. If the number of nodes is not a multiple of k, the leftover
nodes at the end remain in their original order.

Input:
head = [1,2,3,4,5], k = 2

Output:
[2,1,4,3,5]

Input:
head = [1,2,3,4,5], k = 3

Output:
[3,2,1,4,5]
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


def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy               # node just before the current group

    while True:
        # Find the k-th node from group_prev; if missing, stop.
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next    # fewer than k nodes left -> leave as is

        group_next = kth.next        # first node of the next group
        # Reverse the k nodes [group_prev.next .. kth].
        prev, curr = group_next, group_prev.next
        while curr is not group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # group_prev.next was the old head, now the tail of reversed group.
        tail = group_prev.next
        group_prev.next = kth        # connect previous part to new head
        group_prev = tail            # tail leads into the next group


if __name__ == "__main__":
    print(to_list(reverseKGroup(build([1, 2, 3, 4, 5]), 2)))  # Expected: [2, 1, 4, 3, 5]
    print(to_list(reverseKGroup(build([1, 2, 3, 4, 5]), 3)))  # Expected: [3, 2, 1, 4, 5]


'''
Pattern
✅ Reversal (block reversal with a guard for the final partial group)
Check k nodes exist, reverse that block in place, then stitch the prior
tail to the new head and advance. A dummy node anchors the first group.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Better Possible?
❌ No
Each node is visited a constant number of times (counting + reversing),
giving O(n) time and O(1) extra space, which is optimal.
'''
