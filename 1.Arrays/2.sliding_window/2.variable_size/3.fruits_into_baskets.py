'''
3. Fruits Into Baskets (Medium)
Problem Statement

You have two baskets, each holding a single type of fruit. Given an array fruits
where fruits[i] is the type of the i-th tree, pick fruit moving left to right.
Return the length of the longest contiguous run that uses at most 2 fruit types.

(This is "longest subarray with at most 2 distinct values".)

Example
Input:
fruits = [1,2,3,2,2]

Output:
4
Explanation:
[2,3,2,2] uses types {2,3}, length 4.
'''

def totalFruit(fruits):

    count = {}          # fruit type -> count in window
    left = 0
    best = 0

    for right, f in enumerate(fruits):

        count[f] = count.get(f, 0) + 1

        # too many types -> shrink from the left
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(totalFruit([1, 2, 1]))         # Expected: 3
    print(totalFruit([0, 1, 2, 2]))      # Expected: 3
    print(totalFruit([1, 2, 3, 2, 2]))   # Expected: 4

'''
Pattern
✅ Variable-Size Sliding Window (at most K=2 distinct)

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  | (at most 3 types in the map at any time)

Better Possible?
❌ No.
'''
