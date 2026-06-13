'''
2. Custom Sort String (Medium)
Problem Statement

You are given two strings order and s. All characters of order are distinct and
were sorted in some custom order previously. Permute the characters of s so that
they match the order that order was sorted in. Characters of s that do not appear
in order may be appended in any order at the end.

Example
Input:
order = "cba"
s = "abcd"

Output:
"cbad"
'''

def customSortString(order, s):

    # priority[ch] = index in `order`; chars not in order get a large rank
    priority = {ch: i for i, ch in enumerate(order)}
    big = len(order)

    # custom key: ranked chars follow `order`; others share rank `big`
    # and are appended (their relative order among themselves is left as-is).
    chars = sorted(s, key=lambda ch: priority.get(ch, big))

    return "".join(chars)


if __name__ == "__main__":
    print(customSortString("cba", "abcd"))      # Expected: cbad
    print(customSortString("kqep", "pekeq"))     # Expected: kqeep

'''
Pattern
✅ Custom Sorting — lexicographic order defined by an external alphabet

Algorithm & Why
Map each character of `order` to its index, giving the desired priority. Sort the
characters of s by that priority; characters absent from `order` map to a constant
rank past the end, so they land after the ordered group. Timsort's stability keeps
the appended (unordered) chars in their original relative sequence.

| Metric | Value                |
| ------ | -------------------- |
| Time   | O(n log n)           |
| Space  | O(n)                 |
| Stable | Yes (Timsort key)    |

Better Possible?
✅ Count the characters of s and rebuild the string by walking `order` then dumping
leftovers — O(n + |order|) with no comparisons. The key-sort is shorter and clear.
'''
