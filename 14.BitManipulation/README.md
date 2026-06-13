# Bit Manipulation

Pattern-based roadmap for **bit manipulation**. Each numbered folder is one pattern with a
`notes.txt` (sub-pattern tree, template, problems checklist). When built out, a pattern is split
into sub-folders — same structure as [../1.Arrays](../1.Arrays/) … [../13.Greedy](../13.Greedy/).

> The toolkit: set `n|=(1<<i)`, clear `n&=~(1<<i)`, toggle `n^=(1<<i)`, check `(n>>i)&1`,
> lowest set `n&-n`, clear lowest `n&(n-1)`, power-of-2 `n&(n-1)==0`. FAANG focus: Fundamentals,
> XOR, Masking, Subset Enumeration, Prefix XOR, Counting.
>
> Overlap (cross-referenced): Single Number / Missing Number / XOR-of-Range →
> [../1.Arrays/11.advanced/2.bit_manipulation](../1.Arrays/11.advanced/2.bit_manipulation/); Subsets →
> [../8.Recursion/2.backtracking](../8.Recursion/2.backtracking/); Bitmask DP (TSP, Partition to K) →
> [../12.DynamicProgramming/10.bitmask](../12.DynamicProgramming/10.bitmask/); Bitwise Trie (Max/Min XOR) →
> [../11.Trie/5.bitwise](../11.Trie/5.bitwise/); SOS DP → [../12.DynamicProgramming/15.optimization](../12.DynamicProgramming/15.optimization/).

## Patterns

Built **self-contained**. Pattern 9 (Bitwise Trie) is fully cross-referenced to Trie/Arrays.

| #  | Pattern | Folder | Status |
|----|---------|--------|--------|
| 1  | Bit Fundamentals | [1.fundamentals](1.fundamentals/) | 3 problems (bit ops, Number of 1 Bits, Reverse Bits) |
| 2  | XOR Pattern | [2.xor](2.xor/) | 2 problems (Single Number II, III) + cross-refs |
| 3  | Bit Masking | [3.masking](3.masking/) | 1 problem (permission system) |
| 4  | Subset Enumeration | [4.subset_enumeration](4.subset_enumeration/) | 2 problems (subsets, submask enumeration) |
| 5  | Bit Counting | [5.counting](5.counting/) | 3 problems (Counting Bits, Hamming + Total Hamming) |
| 6  | Shift Operations | [6.shift](6.shift/) | 2 problems (Divide / Sum Two Integers) |
| 7  | Range / Prefix XOR | [7.prefix_xor](7.prefix_xor/) | 2 problems (XOR Queries, equal-XOR triplets) |
| 8  | Bitmask DP | [8.bitmask_dp](8.bitmask_dp/) | 2 problems (Can I Win, Matchsticks to Square) |
| 9  | Bitwise Trie | [9.bitwise_trie](9.bitwise_trie/) | cross-ref → Trie/Arrays |
| 10 | Mathematical Tricks | [10.math_tricks](10.math_tricks/) | 3 problems (Power of Two/Four, Number Complement) |
| 11 | Greedy + Bits | [11.greedy_bits](11.greedy_bits/) | 1 problem (Minimize XOR) |
| 12 | Advanced | [12.advanced](12.advanced/) | 1 problem (Gray Code) |

**Total: 22 problems**, every file runnable and verified.

See [notes.txt](notes.txt) for the full roadmap tree, the bit toolkit, and cross-references.

## How to add a problem

1. Pick the right pattern folder (and sub-folder once built out).
2. Create `N.problem_name.py` (N = next number in that folder).
3. Follow the file template below.
4. Tick the box in that folder's `notes.txt` checklist.

### Per-problem file template

```python
'''
N. Problem Title (Difficulty)
Problem Statement

<what the problem asks>

Example
Input:  ...
Output: ...
'''

def solution(...):
    ...


if __name__ == "__main__":
    print(solution(...))   # Expected: ...

'''
Pattern
✅ <which bit trick and why>

| Metric | Value |
| ------ | ----- |
| Time   | O(?)  |
| Space  | O(?)  |

Better Possible?
❌/✅ <reasoning>
'''
```

### How to run any file

```powershell
python "14.BitManipulation\<folder>\<file>.py"
```

Or open the file in VS Code and press `Ctrl+F5` (Run Without Debugging).
