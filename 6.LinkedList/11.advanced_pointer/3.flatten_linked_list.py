'''
Flatten a Linked List (Medium)
Problem Statement

You are given a linked list where every node represents a sub-linked-list and
contains two pointers:
  - next   : points to the next node (head of the next sub-list) on the top level
  - bottom : points to the next node within the same sub-list

Each sub-list (connected via bottom pointers) is sorted in increasing order, and
the top-level next pointers are also in increasing order of their heads. FLATTEN
the structure into a SINGLE sorted linked list connected entirely via the bottom
pointer (next pointers in the result should be None).

Input (top via next, depth via bottom):
5 -> 10 -> 19 -> 28
|     |     |     |
7    20    22    35
|           |     |
8           50    40
|                 |
30                45

Output (flattened, sorted, bottom-linked):
[5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]

Explanation:
Merge all sorted sub-lists into one sorted sub-list along bottom pointers.
'''

# Node carries next (top level) plus an EXTRA bottom pointer (within a sub-list).
class ListNode:
    def __init__(self, val=0, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom


def build_sublist(values):
    # Build one sorted sub-list connected via bottom pointers.
    dummy = cur = ListNode()
    for v in values:
        cur.bottom = ListNode(v)
        cur = cur.bottom
    return dummy.bottom


def build(sublists):
    # sublists: list of value-lists; link their heads via next.
    heads = [build_sublist(s) for s in sublists]
    for i in range(len(heads) - 1):
        heads[i].next = heads[i + 1]
    return heads[0] if heads else None


def to_list(head):
    # Read the flattened result along bottom pointers.
    out = []
    while head:
        out.append(head.val)
        head = head.bottom
    return out


def merge_two(a, b):
    # Merge two bottom-linked sorted lists into one (via bottom).
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.bottom = a
            a = a.bottom
        else:
            tail.bottom = b
            b = b.bottom
        tail = tail.bottom
    tail.bottom = a if a else b
    return dummy.bottom


def flatten(head):
    if not head or not head.next:
        return head
    # Flatten the rest first, then merge the current sub-list into it.
    merged = flatten(head.next)
    head.next = None
    return merge_two(head, merged)


if __name__ == "__main__":
    head = build([
        [5, 7, 8, 30],
        [10, 20],
        [19, 22, 50],
        [28, 35, 40, 45],
    ])
    print(to_list(flatten(head)))
    # Expected: [5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]


'''
Pattern
✅ Advanced Pointer Manipulation — merge along an extra (bottom) pointer

Technique & why:
Each sub-list is already sorted, so flattening is a repeated 2-way merge (like
merging K sorted lists). Recurse to flatten everything to the right into one
sorted bottom-linked list, then merge the current head's sub-list into it. All
linking is done via the bottom pointer; next pointers are dropped.

Let N = total nodes, k = number of sub-lists.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(N * k)   |
| Space  | O(k)       |

Better Possible?
✅ Yes. The sequential merge re-scans accumulated nodes, costing O(N*k). Using a
min-heap of the k current heads (push/pop by value) yields O(N log k) time with
O(k) space, which is optimal for merging k sorted lists.
'''
