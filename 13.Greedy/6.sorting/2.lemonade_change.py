'''
2. Lemonade Change (Easy)
Problem Statement

At a lemonade stand each drink costs $5. Customers queue up and pay with a $5, $10,
or $20 bill (given in order in the array bills). You start with no change. For each
customer you must give back correct change ($0, $5, or $15) using only bills you have
already collected. Return True if you can serve every customer, else False.

Example
Input:
bills = [5, 5, 5, 10, 20]

Output:
True

Explanation:
Collect three $5s, give one back for the $10, then give $5 + $10 for the $20.
'''

def lemonadeChange(bills):

    # Track only how many $5 and $10 bills are on hand ($20s are never used as change).
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            # No change needed; bank the five.
            fives += 1
        elif bill == 10:
            # Owe $5 change.
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # bill == 20, owe $15 change
            # Greedy rule: prefer a 10 + 5 over three 5s, hoarding flexible $5s.
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False

    return True


if __name__ == "__main__":
    print(lemonadeChange([5, 5, 5, 10, 20]))    # Expected: True
    print(lemonadeChange([5, 5, 10, 10, 20]))   # Expected: False

'''
Pattern
Sorting Greedy (process in order; spend the larger denomination first)

Greedy rule & why it's safe
A $10 bill can only ever be used as change for a $20; a $5 bill is change for both
$10 and $20. So when making $15 change, pay with a $10 + $5 before resorting to
three $5s — this preserves the more versatile $5s for future customers.
Exchange argument: if a $10 is available, any solution that pays $15 with three $5s
instead can be rewritten to use the $10 + one $5; this consumes two fewer $5s and one
more (otherwise useless) $10, which can never hurt a later transaction. Hence the
greedy choice dominates, and if greedy fails no other change-making order could
succeed either.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |  (single pass; no sort needed since bills arrive in queue order)
| Space  | O(1)  |  (two counters)

Better Possible?
No — every customer must be inspected once, so O(n) time is optimal and the extra
space is already constant.
'''
