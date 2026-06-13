'''
2. Count Primes (Medium)
Problem Statement

Given an integer n, count the number of primes strictly less than n.

Example
Input:
n = 10

Output:
4
Explanation:
2, 3, 5, 7
'''

def countPrimes(n):

    if n < 3:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes: cross off multiples starting at i*i
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n, i):
                is_prime[multiple] = False

    return sum(is_prime)


if __name__ == "__main__":
    print(countPrimes(10))   # Expected: 4
    print(countPrimes(0))    # Expected: 0
    print(countPrimes(1))    # Expected: 0
    print(countPrimes(20))   # Expected: 8

'''
Pattern
✅ Sieve of Eratosthenes

Key Observation
Mark composites by sweeping multiples of each prime. Start at i*i (smaller multiples
already marked) and stop the outer loop at sqrt(n).

| Metric | Value           |
| ------ | --------------- |
| Time   | O(n log log n)  |
| Space  | O(n)            |

Better Possible?
Segmented / linear sieves exist but this is the standard optimal-enough answer.
'''
