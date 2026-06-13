"""
1094. Car Pooling (Medium)

Problem Statement
-----------------
There is a car with `capacity` empty seats. The vehicle only drives east
(it cannot turn around and drive west).

You are given `trips` where trips[i] = [numPassengers, from, to] means the
i-th trip has `numPassengers` passengers who want to be picked up at location
`from` and dropped off at location `to`. The locations are the distances east
of the car's starting position.

Return True if and only if it is possible to pick up and drop off all
passengers for all the given trips without exceeding capacity at any point.

Example
-------
Input:  trips = [[2,1,5],[3,3,7]], capacity = 4
Output: False
        (at location 3..5 we carry 2 + 3 = 5 passengers > 4)

Input:  trips = [[2,1,5],[3,3,7]], capacity = 5
Output: True

Input:  trips = [[2,1,5],[3,5,7]], capacity = 3
Output: True
        (first trip drops off at 5 exactly when the second picks up at 5)
"""

# ---------------------------------------------------------------------------
# Solution: difference array / coordinate sweep
# ---------------------------------------------------------------------------
# A trip [n, s, e] adds n passengers on the half-open interval [s, e):
# they board at s and leave at e, so location e is already free.
#
# Build a "delta" map: +n at s, -n at e. Sweep the timeline (locations) in
# sorted order, maintaining a running occupancy. If occupancy ever exceeds
# capacity, the answer is False.
#
# GREEDY / SWEEP RULE: process boundary events in increasing location order,
# and at a tie apply drop-offs (-n) before pick-ups (+n). Because we model the
# interval as half-open [s, e), the natural sum of deltas at a coordinate
# already does drops-then-adds when we accumulate all deltas keyed at the same
# location together (a drop at location L and a pickup at L net out before we
# compare to capacity). This is SAFE because occupancy only changes at trip
# endpoints; between consecutive distinct endpoints it is constant, so checking
# the running total at every endpoint checks every location. No future trip can
# lower the count at an earlier location, so a local capacity violation is a
# true, irreversible failure -> the greedy "fail fast" decision is correct.


def car_pooling(trips, capacity):
    # Map location -> net passenger change at that location.
    delta = {}
    for num, start, end in trips:
        delta[start] = delta.get(start, 0) + num   # board
        delta[end] = delta.get(end, 0) - num        # leave
    # Sweep locations left to right. Summing all deltas keyed at the same
    # location handles the "drop before pick up at the same point" tie
    # correctly (drop -n and pick +n combine before the capacity check).
    onboard = 0
    for loc in sorted(delta):
        onboard += delta[loc]
        if onboard > capacity:
            return False
    return True


if __name__ == "__main__":
    print(car_pooling([[2, 1, 5], [3, 3, 7]], 4))   # Expected: False
    print(car_pooling([[2, 1, 5], [3, 3, 7]], 5))   # Expected: True
    print(car_pooling([[2, 1, 5], [3, 5, 7]], 3))   # Expected: True

"""
Pattern
-------
Resource Allocation via difference-array / coordinate sweep.

Greedy rule & why it's safe:
  Treat each trip as a half-open interval [from, to) carrying `num` riders.
  Record +num at the boarding location and -num at the drop location, then
  sweep locations in increasing order accumulating a running occupancy. We
  greedily declare failure the instant occupancy exceeds capacity. This is
  safe because: (1) occupancy is piecewise-constant and only changes at trip
  endpoints, so checking every endpoint checks every location; (2) deltas are
  additive and order-independent within a single location, and modeling
  intervals as half-open makes a drop at L and a pickup at L net out before the
  check -- exactly the LC1094 "drop before board" tie rule; (3) no later event
  can reduce the peak at an earlier location, so the first violation is
  permanent and returning False immediately is correct.

Cross-reference: the min-heap "reuse earliest-free resource" template
  (Meeting Rooms II / Minimum Platforms) computes the PEAK concurrency to size
  the resource; here capacity is fixed, so the sweep just checks the peak
  against it -- same peak-overlap idea, simpler feasibility check.

| Metric | Value          |
|--------|----------------|
| Time   | O(n log n)     |  sort distinct endpoints (n = number of trips)
| Space  | O(n)           |  delta map over endpoints

Better Possible?
  If location values are bounded (LC1094 caps to <= 1000), a fixed-size
  difference array indexed by location gives O(n + maxLoc) time and
  O(maxLoc) space -- linear, dropping the sort. For unbounded coordinates the
  O(n log n) sweep above is essentially optimal.
"""
