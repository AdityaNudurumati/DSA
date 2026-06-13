'''
1. Print Linked List in Reverse (Recursive) (Easy)
Problem Statement

Given the head of a singly linked list, return its values in reverse order
using recursion (recurse first, then record the current value on the way back
up the call stack).

Input:
head = [1, 2, 3, 4, 5]

Output:
[5, 4, 3, 2, 1]
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


def reverse_values(head):
    # Recurse to the tail first, then append on the unwind -> reversed order.
    result = []

    def recurse(node):
        if node is None:
            return
        recurse(node.next)      # go deeper first
        result.append(node.val)  # record on the way back up

    recurse(head)
    return result


if __name__ == "__main__":
    head1 = build([1, 2, 3, 4, 5])
    print(reverse_values(head1))  # Expected: [5, 4, 3, 2, 1]


'''
Pattern
✅ Recursive Traversal (post-order)
Descend to the end of the list before doing any work, then process each node as
the stack unwinds. Because the last node finishes its recursion first, values
are collected tail-to-head, yielding reverse order without mutating the list.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(n)  |  (recursion call stack)

Better Possible?
✅ Yes (on space)
An iterative pass that pushes values onto an explicit stack, or that walks once
and reverses the collected list, achieves the same O(n) time with O(1) auxiliary
space if we reverse in place. The recursive form is the clearest expression of
the pattern but pays O(n) stack space (and risks recursion-limit overflow on
very long lists).
'''
