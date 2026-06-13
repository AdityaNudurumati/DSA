'''
24. Swap Nodes in Pairs (Medium)
Problem Statement

Given the head of a linked list, swap every two adjacent nodes and return the
head of the modified list. You must swap the actual nodes (not just their values).

A dummy node before the head removes the edge case of swapping the first pair,
since the node preceding each pair is then always available.

Example:
Input:  head = [1,2,3,4]
Output: [2,1,4,3]

Input:  head = [1,2,3]
Output: [2,1,3]
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
def swapPairs(head):
    dummy = ListNode(0, head)      # dummy precedes the first pair
    prev = dummy
    # prev is the node before the pair (first, second) we are about to swap
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        # rewire: prev -> second -> first -> rest
        first.next = second.next
        second.next = first
        prev.next = second
        # first is now the tail of the swapped pair; move prev there
        prev = first
    return dummy.next


if __name__ == "__main__":
    print(to_list(swapPairs(build([1, 2, 3, 4]))))  # Expected: [2, 1, 4, 3]
    print(to_list(swapPairs(build([1, 2, 3]))))     # Expected: [2, 1, 3]


'''
Pattern
✅ Dummy Node
The dummy guarantees a real "prev" node before the first pair, so swapping the
head pair uses the same three pointer rewires as any other pair. Each step splices
(prev -> second -> first -> rest) and advances prev to the tail of the swapped pair.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Each node is visited once and relinked in place; O(n) time / O(1) space is
optimal. A recursive version is also O(n) but uses O(n) stack space.
'''
