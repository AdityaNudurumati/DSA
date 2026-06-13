'''
2. Two-Pass Stable Sort by (Major, Minor) Keys (Medium)
Problem Statement

To sort records by a composite key (major, minor) using single-key stable passes,
sort by the MINOR key first, then by the MAJOR key. Because the second pass is STABLE,
records that tie on the major key keep the order the minor pass gave them — so the
minor ordering survives as the tiebreaker.

Given student records [("CS",90),("Math",85),("CS",80),("Math",85)], sort by
(department ascending, score descending).

Input:
records = [("CS",90),("Math",85),("CS",80),("Math",85)]
order   = dept asc, then score desc

Output:
[("CS",90),("CS",80),("Math",85),("Math",85)]

Explanation:
Pass 1 (minor = score, DESCENDING, stable):
  [("CS",90),("Math",85),("Math",85),("CS",80)]
  the two Math/85 ties keep their input order.
Pass 2 (major = dept, ASCENDING, stable):
  CS records come before Math records; within each dept the score order from pass 1
  is preserved -> [("CS",90),("CS",80),("Math",85),("Math",85)].
'''


def stable_sort(records, key, reverse=False):
    # Stable insertion sort by hand on a single key.
    # Equality never triggers a shift, so equal keys keep their relative order.
    arr = list(records)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        if not reverse:
            # ascending: shift while previous key strictly greater
            while j >= 0 and key(arr[j]) > key(current):
                arr[j + 1] = arr[j]
                j -= 1
        else:
            # descending: shift while previous key strictly smaller
            while j >= 0 and key(arr[j]) < key(current):
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = current
    return arr


def two_pass_sort(records):
    # Pass 1: minor key (score) descending.
    by_minor = stable_sort(records, key=lambda r: r[1], reverse=True)
    # Pass 2: major key (dept) ascending. Stability preserves the score order on ties.
    by_major = stable_sort(by_minor, key=lambda r: r[0], reverse=False)
    return by_major


if __name__ == "__main__":
    records = [("CS", 90), ("Math", 85), ("CS", 80), ("Math", 85)]
    print(two_pass_sort(records))  # Expected: [('CS', 90), ('CS', 80), ('Math', 85), ('Math', 85)]


'''
Pattern
✅ Secondary Key Preservation (multi-pass stable sort)
Sort by the LEAST significant key first and the MOST significant key last, each pass
stable. The last pass dominates the ordering; stability lets earlier passes act as
tiebreakers. This is exactly the idea behind LSD radix sort.

| Metric | Value          |
| ------ | -------------- |
| Time   | O(p * n^2)     |  (p passes; here insertion sort per pass)
| Space  | O(n)           |
| Stable | Yes            |

Better Possible?
✅ Yes.
Use a stable O(n log n) sort per pass (merge/Timsort) for O(p * n log n). Or, when the
keys can be compared directly, a single sort with a composite key tuple
— sorted(records, key=lambda r: (r[0], -r[1])) — does it in one O(n log n) pass.
'''
