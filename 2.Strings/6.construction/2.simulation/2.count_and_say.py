'''
2. Count and Say (Medium)
Problem Statement

The count-and-say sequence is defined as follows:
- countAndSay(1) = "1"
- countAndSay(n) is the "run-length encoding" said aloud of countAndSay(n-1).

To say a string, count the number of each group of consecutive identical
digits, then say the count followed by the digit. For example "3322251"
is said as "two 3s, three 2s, one 5, one 1" = "23"+"32"+"15"+"11" = "23321511".

Return the nth term of the sequence.

Example
Input:
n = 4

Output:
"1211"
'''

def countAndSay(n):
    result = "1"   # base case: countAndSay(1)

    # build each term from the previous one
    for _ in range(n - 1):
        next_term = []
        i = 0
        while i < len(result):
            count = 1
            # count the run of identical digits starting at i
            while i + 1 < len(result) and result[i] == result[i + 1]:
                count += 1
                i += 1
            next_term.append(str(count))   # say the count
            next_term.append(result[i])    # then the digit
            i += 1
        result = ''.join(next_term)

    return result


if __name__ == "__main__":
    print(countAndSay(1))  # Expected: 1
    print(countAndSay(4))  # Expected: 1211
    print(countAndSay(5))  # Expected: 111221


'''
Pattern
✅ Simulation (run-length encode the previous term repeatedly)
Each term is produced by scanning the previous term, counting consecutive
runs of the same digit, and emitting count+digit.

| Metric | Value                       |
| ------ | --------------------------- |
| Time   | O(n * L)  (L = term length) |
| Space  | O(L)                        |

Better Possible?
❌ No closed form for general n — terms grow ~1.3x each step (Conway's
constant), so generating them in order is required.
'''
