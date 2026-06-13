'''
2. Search Value in Linked List (Easy)
Problem Statement

Given the head of a singly linked list and a target value, return True if the
value exists in the list, otherwise return False.

Input:
head = [1, 2, 3], target = 2

Output:
True

Example 2:
Input:
head = [1, 2, 3], target = 5
Output:
False
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


def search_value(head, target):
    # Walk the list; return True as soon as a matching value is found.
    curr = head
    while curr:
        if curr.val == target:
            return True
        curr = curr.next
    return False


if __name__ == "__main__":
    head1 = build([1, 2, 3])
    print(search_value(head1, 2))  # Expected: True

    head2 = build([1, 2, 3])
    print(search_value(head2, 5))  # Expected: False


'''
Pattern
✅ Basic Iterative Traversal (linear search)
Scan node-by-node and short-circuit the moment the target matches. A singly
linked list has no random access, so linear scan is the only option.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No
For an unsorted, non-indexable linked list, any value may sit at the tail, so
O(n) worst-case comparisons are unavoidable. Optimal.
'''
