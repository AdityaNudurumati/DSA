'''
21. Merge Two Sorted Lists (Easy)
Problem Statement

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list by splicing together the nodes of the
two lists. Return the head of the merged linked list.

Example
Input:
list1 = [1,2,4], list2 = [1,3,4]

Output:
[1,1,2,3,4,4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def build(values):                       # list -> linked list
    dummy = cur = ListNode()
    for v in values:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next

def to_list(head):                       # linked list -> list
    out = []
    while head:
        out.append(head.val); head = head.next
    return out


def mergeTwoLists(a, b):
    # dummy node lets us build the result without special-casing the head
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:               # pick smaller front, advance that list
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b                   # attach whatever remains (one is None)
    return dummy.next


if __name__ == "__main__":
    print(to_list(mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))
    # Expected: [1, 1, 2, 3, 4, 4]
    print(to_list(mergeTwoLists(build([]), build([]))))       # Expected: []
    print(to_list(mergeTwoLists(build([]), build([0]))))      # Expected: [0]

'''
Pattern
✅ Two pointers + dummy node (the canonical merge step of merge sort)

Key Observation
Walk both sorted lists with one pointer each; repeatedly splice the smaller front
node onto the tail of the result. A dummy head removes the "which list owns the
first node" edge case, and `tail.next = a or b` cheaply appends the leftover run.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(m + n)   |
| Space  | O(1)       | (splices existing nodes, no new list)

Better Possible?
❌ No. Every node must be visited once, so O(m + n) is optimal.
'''
