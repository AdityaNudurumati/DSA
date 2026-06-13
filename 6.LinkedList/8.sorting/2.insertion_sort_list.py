'''
147. Insertion Sort List (Medium)
Problem Statement

Given the head of a singly linked list, sort the list using insertion sort and
return the sorted list's head.

Insertion sort iterates over the input nodes one at a time and, for each node,
finds its correct position in an already-sorted prefix and splices it in.

Example:
Input:  head = [4,2,1,3]
Output: [1,2,3,4]

Input:  head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):           # list -> head
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):           # head -> list
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def insertionSortList(head):
    dummy = ListNode()       # sorted list grows off this dummy head
    cur = head
    while cur:
        nxt = cur.next       # remember the next node to process

        # find the last node in the sorted part smaller than cur
        prev = dummy
        while prev.next and prev.next.val < cur.val:
            prev = prev.next

        # splice cur between prev and prev.next
        cur.next = prev.next
        prev.next = cur

        cur = nxt            # advance to the next unsorted node
    return dummy.next


if __name__ == "__main__":
    print(to_list(insertionSortList(build([4, 2, 1, 3]))))      # Expected: [1, 2, 3, 4]
    print(to_list(insertionSortList(build([-1, 5, 3, 4, 0]))))  # Expected: [-1, 0, 3, 4, 5]


'''
Pattern
✅ Insertion Sort with a Dummy Head
Maintain a sorted list behind a dummy node. For each input node, walk the sorted
part to find its insertion point and rewire pointers to splice it in. The dummy
node removes the special-case of inserting at the front.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^2) |
| Space  | O(1)   |

Better Possible?
✅ Yes — insertion sort is O(n^2). Merge sort (see 1.sort_list.py) sorts a
linked list in O(n log n), which is the optimal comparison-sort bound.
'''
