'''
430. Flatten a Multilevel Doubly Linked List (Medium)
Problem Statement

You are given a doubly linked list, which contains nodes that have a next
pointer, a previous pointer, and an additional child pointer. This child pointer
may or may not point to a separate doubly linked list, also containing these
special nodes. These child lists may have one or more children of their own, and
so on, producing a multilevel data structure.

Given the head of the first level of the list, FLATTEN the list so that all the
nodes appear in a single-level, doubly linked list. Let curr be a node with a
child list. The nodes in the child list should appear after curr and before
curr.next in the flattened list. Set all child pointers to None.

Input (multilevel):
1 - 2 - 3 - 4 - 5 - 6
        |
        7 - 8 - 9 - 10
            |
            11 - 12

Output:
[1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

Explanation:
At node 3 we descend into [7,8,9,10]; at node 8 we descend into [11,12]; each
child list is spliced in immediately after its parent, then we continue.
'''

# Node carries prev/next (doubly linked) plus an EXTRA child pointer.
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def build(values):
    # Build a flat doubly linked list (no children) from a list of values.
    dummy = cur = Node()
    for v in values:
        node = Node(v)
        node.prev = cur
        cur.next = node
        cur = node
    head = dummy.next
    if head:
        head.prev = None
    return head


def attach_child(node, child_head):
    # Helper: hang an existing sub-list as node.child.
    node.child = child_head
    return node


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def flatten(head):
    if not head:
        return None

    cur = head
    while cur:
        if cur.child:
            # Remember what comes after the current node on this level.
            nxt = cur.next
            child = cur.child

            # Splice the child list in right after cur.
            cur.next = child
            child.prev = cur
            cur.child = None

            # Walk to the tail of the (still single-level) child list.
            tail = child
            while tail.next:
                tail = tail.next

            # Re-attach the saved remainder after the child's tail.
            tail.next = nxt
            if nxt:
                nxt.prev = tail
        cur = cur.next
    return head


if __name__ == "__main__":
    # Build level 1: 1-2-3-4-5-6
    head = build([1, 2, 3, 4, 5, 6])
    # Build level 2 under node 3: 7-8-9-10
    level2 = build([7, 8, 9, 10])
    # Build level 3 under node 8: 11-12
    level3 = build([11, 12])

    # Locate node 3 and node 8 to attach children.
    node3 = head
    while node3.val != 3:
        node3 = node3.next
    node8 = level2
    while node8.val != 8:
        node8 = node8.next

    attach_child(node3, level2)
    attach_child(node8, level3)

    print(to_list(flatten(head)))  # Expected: [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]


'''
Pattern
✅ Advanced Pointer Manipulation — iterative DFS splice

Technique & why:
Walk the list; whenever a node has a child, splice the entire child list between
the node and its successor, then rewire prev pointers and clear the child link.
Continuing from the spliced-in node naturally handles deeper nesting (a child's
own child is reached later in the same forward walk), giving a depth-first order
without recursion or a stack.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No. Every node must be visited and relinked once, so O(n) time is optimal, and
the in-place splicing uses only O(1) auxiliary space (a recursive/stack solution
would add O(depth) space).
'''
