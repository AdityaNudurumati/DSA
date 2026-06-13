'''
N. Reverse Alternate K Nodes (Medium)
Problem Statement

Given the head of a singly linked list and an integer k, reverse every
alternate block of k nodes: reverse the first k, leave the next k as is,
reverse the following k, and so on. If a block to reverse has fewer than
k nodes, reverse whatever remains.

Input:
head = [1,2,3,4,5,6,7,8], k = 2

Output:
[2,1,3,4,6,5,7,8]

Explanation:
reverse [1,2] -> [2,1]; skip [3,4]; reverse [5,6] -> [6,5]; skip [7,8].
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


def reverseAlternateK(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy               # node before the block being reversed

    while group_prev.next:
        # ---- reverse up to k nodes starting at group_prev.next ----
        prev = None
        curr = group_prev.next
        first = curr                 # becomes the tail after reversal
        count = 0
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        group_prev.next = prev       # connect to new head of reversed block
        first.next = curr            # tail links to the skipped section
        group_prev = first           # tail precedes the skip block

        # ---- skip the next k nodes (leave them untouched) ----
        for _ in range(k):
            if not group_prev.next:
                break
            group_prev = group_prev.next

    return dummy.next


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5, 6, 7, 8])
    print(to_list(reverseAlternateK(head, 2)))  # Expected: [2, 1, 3, 4, 6, 5, 7, 8]


'''
Pattern
✅ Reversal (alternating reverse-k / skip-k blocks)
Reuse the standard k-block reverse, then walk k nodes forward without
touching them, repeating until the list ends. A dummy node anchors the
first reversed block.
| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |
Better Possible?
❌ No
Every node is processed once (reversed or skipped); O(n) time with O(1)
extra space is optimal.
'''
