'''
2. Reverse Pairs (Hard)
Problem Statement

Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].

Example
Input:
nums = [1,3,2,3,1]

Output:
2
'''

def reversePairs(nums):

    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, lc = sort_count(a[:mid])
        right, rc = sort_count(a[mid:])

        # count cross pairs BEFORE merging, using that both halves are sorted
        count = 0
        j = 0
        for x in left:
            while j < len(right) and x > 2 * right[j]:
                j += 1
            count += j

        return merge(left, right), lc + rc + count

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    _, total = sort_count(nums)
    return total


if __name__ == "__main__":
    print(reversePairs([1, 3, 2, 3, 1]))   # Expected: 2
    print(reversePairs([2, 4, 3, 5, 1]))   # Expected: 3

'''
Pattern
✅ Merge Sort with a separate cross-pair count

Key Observation
With both halves sorted, a two-pointer sweep counts how many right elements satisfy
nums[i] > 2*nums[j] for each left element, in linear time per merge. Count first,
then merge normally.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |
| Space  | O(n)       |

Better Possible?
❌ No (also solvable with a BIT / merge sort; same complexity).
'''
