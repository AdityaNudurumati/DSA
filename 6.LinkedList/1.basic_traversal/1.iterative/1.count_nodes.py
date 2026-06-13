'''
1. Count Nodes / Get Length (Easy)
Problem Statement

Given the head of a singly linked list, count and return the number of nodes
in the list (its length).

Input:
head = [1, 2, 3, 4, 5]

Output:
5

Example 2:
Input:
head = []
Output:
0
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):
    # Build a singly linked list from a Python list; return its head.
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    # Convert a linked list back to a Python list of values.
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def count_nodes(head):
    # Walk the list once, incrementing a counter per node.
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count


if __name__ == "__main__":
    head1 = build([1, 2, 3, 4, 5])
    print(count_nodes(head1))  # Expected: 5

    head2 = build([])
    print(count_nodes(head2))  # Expected: 0


'''
Pattern
✅ Basic Iterative Traversal
Move a single pointer from head to None, tallying each visited node. This is the
canonical "walk the list once" loop that underlies every list algorithm.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
Length is not stored, so every node must be visited at least once. O(n) is optimal.
(Maintaining a size field on the list structure could make it O(1), but that is a
different data-structure design, not a traversal improvement.)
'''
