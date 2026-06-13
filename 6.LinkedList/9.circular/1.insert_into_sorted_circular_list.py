'''
708. Insert into a Sorted Circular Linked List (Medium)
Problem Statement

Given a node from a Circular Linked List which is sorted in non-decreasing
order, write a function to insert a value insertVal into the list such that it
remains a sorted circular list. The given node can be any single node in the
list and may not necessarily be the smallest value.

If there are multiple suitable places for insertion, you may choose any. After
insertion, the circular list should remain sorted. If the list is empty (a null
pointer is given), create a new single circular node and return it.

Example:
Input:  circular list [3, 4, 1], insertVal = 2
Output: [1, 2, 3, 4]   (reading one loop starting from the smallest value)
Explanation:
The ring is 3 -> 4 -> 1 -> (back to 3). Inserting 2 between 1 and 3 keeps the
ring sorted. Printed from the smallest node it reads 1, 2, 3, 4.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build_circular(values):
    # Build a circular singly linked list; tail.next loops back to head.
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = head  # close the ring
    return head


def to_list_from_smallest(head):
    # Walk the whole ring once, then rotate output to start at the min value.
    if not head:
        return []
    vals = [head.val]
    curr = head.next
    while curr is not head:
        vals.append(curr.val)
        curr = curr.next
    i = vals.index(min(vals))
    return vals[i:] + vals[:i]


def insert(head, insertVal):
    node = ListNode(insertVal)

    # Case 1: empty list -> single node pointing to itself.
    if not head:
        node.next = node
        return node

    prev, curr = head, head.next
    while True:
        # Case 2: normal slot between two ascending values.
        if prev.val <= insertVal <= curr.val:
            break
        # Case 3: at the rotation point (max -> min boundary).
        # Insert if value is a new max (after max) or new min (before min).
        if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
            break
        prev, curr = curr, curr.next
        # Case 4: looped fully (all values equal) -> insert anywhere.
        if prev is head:
            break

    prev.next = node
    node.next = curr
    return head


if __name__ == "__main__":
    # Example 1: insert 2 into [3,4,1]
    head = build_circular([3, 4, 1])
    head = insert(head, 2)
    print(to_list_from_smallest(head))            # Expected: [1, 2, 3, 4]

    # Example 2: insert into empty list
    head = insert(None, 5)
    print(to_list_from_smallest(head))            # Expected: [5]

    # Example 3: new max (wrap-around, after max)
    head = build_circular([1, 3, 5])
    head = insert(head, 6)
    print(to_list_from_smallest(head))            # Expected: [1, 3, 5, 6]

    # Example 4: new min (wrap-around, before min)
    head = build_circular([1, 3, 5])
    head = insert(head, 0)
    print(to_list_from_smallest(head))            # Expected: [0, 1, 3, 5]

    # Example 5: all-equal ring, insert anywhere
    head = build_circular([2, 2, 2])
    head = insert(head, 2)
    print(to_list_from_smallest(head))            # Expected: [2, 2, 2, 2]


'''
Pattern
Circular Traversal + boundary handling

Technique & why:
Walk the ring with a prev/curr pair exactly once. Three insertion situations
must be detected: (a) the value fits between two ascending neighbours, (b) we
are sitting on the single descending edge (max -> min) and the value is either a
new maximum or a new minimum, and (c) we completed a full loop without finding a
slot (the list is uniform), so we just insert at the start. Stopping after one
loop avoids an infinite circle.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
No. Without random access the correct slot can only be found by scanning the
ring, which is inherently O(n). O(1) extra space is already optimal.
'''
