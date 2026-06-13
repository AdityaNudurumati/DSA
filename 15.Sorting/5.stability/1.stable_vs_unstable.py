'''
1. Stable vs Unstable Sort (Easy)
Problem Statement

A STABLE sort keeps elements with EQUAL keys in their original relative input order.
An UNSTABLE sort makes no such promise: equal-key elements may be reordered.

Given records [(1,'a'),(2,'b'),(1,'c'),(2,'d')], sort by the NUMBER key only.
A stable sort must preserve the input order of ties:
  the two 1's stay as 'a' before 'c', and the two 2's stay as 'b' before 'd'.

Demonstrate a STABLE result and explain.

Input:
records = [(1,'a'),(2,'b'),(1,'c'),(2,'d')]
key = number (first element)

Output:
[(1,'a'),(1,'c'),(2,'b'),(2,'d')]

Explanation:
Among the 1-keys, 'a' appeared before 'c' in the input, so 'a' stays first.
Among the 2-keys, 'b' appeared before 'd', so 'b' stays first.
An UNSTABLE sort might return [(1,'c'),(1,'a'),...] which is still "sorted by number"
but loses the original tie order.
'''


def stable_sort_by_number(records):
    # Stable insertion sort: by hand, comparison based.
    # Insertion sort is stable because we shift only when a key is STRICTLY greater,
    # never on equality, so equal keys never jump over each other.
    arr = list(records)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        # shift right only while previous key is strictly greater (use >, not >=)
        while j >= 0 and arr[j][0] > current[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def unstable_sort_by_number(records):
    # Selection sort with a strict-greater swap of the min is unstable: moving the
    # selected minimum into place can leapfrog an equal-key element. Shown for contrast.
    arr = list(records)
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    records = [(1, 'a'), (2, 'b'), (1, 'c'), (2, 'd')]
    print(stable_sort_by_number(records))    # Expected: [(1, 'a'), (1, 'c'), (2, 'b'), (2, 'd')]


'''
Pattern
✅ Stable Sort (stable insertion sort)
Insertion sort shifts elements only on a STRICTLY-greater comparison, so equal keys
keep their input order — that is exactly what stability means. Multi-key sorting,
ranking, and "sort by score but keep entry order on ties" all rely on this.

| Metric | Value  |
| ------ | ------ |
| Time   | O(n^2) |
| Space  | O(n)   |
| Stable | Yes    |

Better Possible?
✅ Yes — for speed.
A stable O(n log n) sort (merge sort, or Python's Timsort via sorted(arr, key=...))
gives the same stable ordering far faster. Insertion sort is used here only because
its stability is easy to see by hand.
'''
