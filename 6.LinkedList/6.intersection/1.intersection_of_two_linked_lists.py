'''
160. Intersection of Two Linked Lists (Easy)
Problem Statement

Given the heads of two singly linked lists headA and headB, return the node at
which the two lists intersect. If the two linked lists have no intersection at
all, return None.

The intersection is defined by REFERENCE, not by value: the two lists share the
same physical tail node onward (a Y-shape). The lists must keep their original
structure after the function returns.

Example:
Input:
A = [4, 1] -> [8, 4, 5]   (the second part is shared)
B = [5, 6, 1] -> [8, 4, 5]
Output:
8                          (value of the first shared node)

Explanation:
Both lists meet at the node with value 8 and run together to the end.
A non-intersecting pair returns None.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):                       # list -> head of linked list
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):                       # linked list -> list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build_intersecting(a_only, b_only, shared):
    """Build two Y-shaped lists that share the SAME tail nodes (by reference).
    Returns (headA, headB)."""
    tail = build(shared)                 # one physical shared tail
    headA = build(a_only)
    headB = build(b_only)
    # attach the shared tail to the end of each unique prefix
    if headA:
        cur = headA
        while cur.next:
            cur = cur.next
        cur.next = tail
    else:
        headA = tail
    if headB:
        cur = headB
        while cur.next:
            cur = cur.next
        cur.next = tail
    else:
        headB = tail
    return headA, headB


def getIntersectionNode(headA, headB):
    # Two-pointer switch trick: each pointer walks its own list, then hops to
    # the other head. After at most lenA + lenB steps both have traveled the
    # same distance, so they meet at the intersection node (or both at None).
    a, b = headA, headB
    while a is not b:                     # compare by REFERENCE, not value
        a = a.next if a else headB
        b = b.next if b else headA
    return a                             # intersection node, or None


if __name__ == "__main__":
    # Intersecting case: shared tail [8, 4, 5]
    headA, headB = build_intersecting([4, 1], [5, 6, 1], [8, 4, 5])
    node = getIntersectionNode(headA, headB)
    print(node.val if node else None)    # Expected: 8

    # Non-intersecting case: no shared nodes
    a = build([2, 6, 4])
    b = build([1, 5])
    node = getIntersectionNode(a, b)
    print(node.val if node else None)    # Expected: None


'''
Pattern
✅ Intersection — Two-Pointer Switch
Walk pointer a over A then B, and pointer b over B then A. Both traverse
lenA + lenB nodes total, which cancels the length difference, so they land on
the first shared node simultaneously (or on None together if disjoint). No
extra space, no length pre-computation, and the lists are left unmodified.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(m + n)   |
| Space  | O(1)       |

Better Possible?
❌ No
Every node may need inspecting to confirm the join, so O(m + n) time is optimal.
The switch trick already achieves O(1) space, beating the hash-set approach
(O(m) space) and matching the length-alignment approach without extra passes.
'''
