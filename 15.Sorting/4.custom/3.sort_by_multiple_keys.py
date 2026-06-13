'''
3. Sort by Multiple Keys (Easy)
Problem Statement

Given a list of records (name, age), sort them by two keys at once:
name ascending (primary), then age descending (secondary) within the same name.

Example
Input:
people = [("A", 30), ("B", 25), ("A", 20), ("B", 25)]

Output:
[("A", 30), ("A", 20), ("B", 25), ("B", 25)]
'''

def sortByMultipleKeys(people):

    # multi-key sort: name ascending, age descending.
    # negate the numeric secondary key to flip its direction while keeping
    # a single ascending tuple comparison. (Key is the point here, not the sort.)
    return sorted(people, key=lambda rec: (rec[0], -rec[1]))


if __name__ == "__main__":
    print(sortByMultipleKeys([("A", 30), ("B", 25), ("A", 20), ("B", 25)]))
    # Expected: [('A', 30), ('A', 20), ('B', 25), ('B', 25)]
    print(sortByMultipleKeys([("Bob", 40), ("Al", 20), ("Al", 50), ("Bob", 10)]))
    # Expected: [('Al', 50), ('Al', 20), ('Bob', 40), ('Bob', 10)]

'''
Pattern
✅ Custom Sorting — multi-key tuple comparison with mixed directions

Algorithm & Why
Python compares tuples lexicographically, so a key of (primary, secondary) sorts by
primary first and breaks ties by secondary. To sort one numeric key descending while
the rest stay ascending, negate that field (-age). For non-negatable keys you would
instead pass a pairwise functools.cmp_to_key comparator.

| Metric | Value             |
| ------ | ----------------- |
| Time   | O(n log n)        |
| Space  | O(n)              |
| Stable | Yes (Timsort)     |

Better Possible?
❌ No — comparison sorting is Omega(n log n); the multi-key tuple is the canonical
expression of "order by k1 asc, k2 desc".
'''
