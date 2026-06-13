'''
1. Gas Station (Medium)
Problem Statement

There are n gas stations in a circle. gas[i] is the fuel at station i and cost[i]
is the fuel needed to travel from station i to i+1. Starting with an empty tank,
return the index of the station to begin a full clockwise loop, or -1 if impossible.
A unique answer exists if one exists.

Example
Input:
gas = [1,2,3,4,5], cost = [3,4,5,1,2]

Output:
3
'''

def canCompleteCircuit(gas, cost):

    # if total fuel < total cost, no start can complete the loop
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:                 # can't reach i+1 from current start
            start = i + 1            # everything up to i is also invalid
            tank = 0

    return start


if __name__ == "__main__":
    print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))   # Expected: 3
    print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))                # Expected: -1

'''
Pattern
✅ Greedy running balance (reset start on deficit)

Key Observation
If the tank goes negative between start..i, no station in that range can be the
start (each later one starts with even less). Jump start to i+1. Feasibility is
guaranteed by the total-sum check.

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

Better Possible?
❌ No.
'''
