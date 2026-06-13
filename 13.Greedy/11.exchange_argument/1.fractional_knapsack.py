'''
1. Fractional Knapsack (Medium)
Problem Statement

You are given the values and weights of n items, and a knapsack with a weight
capacity. Unlike 0/1 knapsack, you MAY take fractions of an item.

Maximize the total value you can carry without exceeding the capacity.

Example
Input:
values  = [60, 100, 120]
weights = [10,  20,  30]
capacity = 50

Output:
240.0
Explanation:
Take items 1 and 2 fully (value 60 + 100 = 160, weight 30), then 20/30 of item 3
for value 120 * (20/30) = 80. Total = 240.0
'''


def fractional_knapsack(values, weights, capacity):
    # Greedy rule: take items in DECREASING order of value/weight ratio,
    # filling as much of each as fits, and a fraction of the last one.
    items = sorted(
        zip(values, weights),
        key=lambda vw: vw[0] / vw[1],
        reverse=True,
    )

    total = 0.0
    remaining = capacity

    for value, weight in items:
        if remaining <= 0:
            break
        take = min(weight, remaining)          # take whole item, or what's left
        total += take * (value / weight)       # value scales with fraction taken
        remaining -= take

    return total


if __name__ == "__main__":
    print(fractional_knapsack([60, 100, 120], [10, 20, 30], 50))         # Expected: 240.0
    print(fractional_knapsack([60, 40, 100, 120], [10, 40, 20, 30], 50)) # Expected: 240.0


'''
Pattern
Exchange Argument Greedy (sort by value/weight ratio)

Greedy rule & why it's safe
Always spend the next unit of capacity on the item with the highest value-per-weight
ratio. Exchange argument: suppose an optimal solution uses some capacity on a lower-ratio
item while a higher-ratio item is not fully taken. Swap an epsilon of weight from the
lower-ratio item to the higher-ratio one. Value strictly increases (or stays equal),
contradicting optimality. Hence the ratio order is optimal. Fractions are allowed, so
the last item can always be partially filled to use capacity exactly.

| Metric | Value      |
| ------ | ---------- |
| Time   | O(n log n) |  (dominated by the sort)
| Space  | O(n)       |  (sorted copy of items)

Better Possible?
No. Sorting by ratio is the standard optimal approach; you cannot beat O(n log n) in
the comparison model for the general sorted-selection. (0/1 knapsack would be NP-hard,
but the fractional variant is provably greedy-optimal.)
'''
