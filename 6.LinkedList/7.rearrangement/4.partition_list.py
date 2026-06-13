'''
86. Partition List (Medium)
Problem Statement

Given the head of a linked list and a value x, partition it so that all nodes
with value LESS THAN x come before all nodes with value GREATER THAN OR EQUAL TO x.

You must preserve the original relative order of the nodes within each of the two
partitions.

Example:
Input:  head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input:  head = [2,1], x = 2
Output: [1,2]
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


def partition(head, x):
    # Two dummy-headed chains: one for < x, one for >= x.
    less_dummy = less = ListNode()
    geq_dummy = geq = ListNode()

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            geq.next = head
            geq = geq.next
        head = head.next

    geq.next = None              # terminate the >= chain (avoid dangling cycle)
    less.next = geq_dummy.next   # stitch the >= chain after the < chain
    return less_dummy.next


if __name__ == "__main__":
    print(to_list(partition(build([1, 4, 3, 2, 5, 2]), 3)))  # Expected: [1, 2, 2, 4, 3, 5]
    print(to_list(partition(build([2, 1]), 2)))              # Expected: [1, 2]


'''
Pattern
✅ List Rearrangement (dummy-node two-chain split)
Thread each node onto one of two chains (less-than vs. greater-or-equal) in a
single pass, preserving arrival order, then concatenate. Dummy heads remove
edge-case branching for empty chains.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
One pass, constant extra pointers, stable ordering — optimal.
'''
