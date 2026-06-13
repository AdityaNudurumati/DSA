'''
1. Permission System (Easy)
Problem Statement

Design a small permission / flag system where each capability is one bit of an
integer mask. Support: add a permission, remove a permission, check whether a
permission is present (has), combine two masks, and list the set bits.

Permissions:
    READ = bit 0, WRITE = bit 1, EXEC = bit 2

Demo:
    start with empty mask 0
    add READ, add WRITE
    has(READ)  -> True
    has(EXEC)  -> False
    remove(READ)
    has(READ)  -> False
    combine with another mask

Input:
    operations as shown in the demo above

Output:
    True, False, False
'''

# Each capability is a single bit. The whole permission set is ONE int.
READ = 0   # bit 0
WRITE = 1  # bit 1
EXEC = 2   # bit 2

def add(mask, perm):
    # turn a flag ON: set bit at position `perm`
    return mask | (1 << perm)

def remove(mask, perm):
    # turn a flag OFF: clear bit at position `perm` with the inverse mask
    return mask & ~(1 << perm)

def has(mask, perm):
    # test a flag: shift the wanted bit down to position 0 and AND with 1
    return (mask >> perm) & 1 == 1

def combine(mask_a, mask_b):
    # union of two flag sets is just bitwise OR
    return mask_a | mask_b

def list_set_bits(mask):
    # positions of all flags that are ON, low bit first
    return [i for i in range(mask.bit_length()) if (mask >> i) & 1]


if __name__ == "__main__":
    mask = 0                      # start: no permissions
    mask = add(mask, READ)        # grant READ  (bit 0)
    mask = add(mask, WRITE)       # grant WRITE (bit 1)

    print(has(mask, READ))        # Expected: True
    print(has(mask, EXEC))        # Expected: False

    mask = remove(mask, READ)     # revoke READ
    print(has(mask, READ))        # Expected: False

    # combine with another mask that has EXEC -> union keeps WRITE and adds EXEC
    other = add(0, EXEC)
    merged = combine(mask, other)
    print(sorted(list_set_bits(merged)))  # Expected: [1, 2]


'''
Pattern
✅ Bit Masking
Each permission is one bit of an int, so the whole set of flags is a single number.
add = OR with (1<<i), remove = AND with ~(1<<i), has = (mask>>i)&1, combine = OR.
This turns set membership/union/insert/delete into O(1) bitwise ops instead of a
list of booleans or a hash set.
| Metric | Value |
| ------ | ----- |
| Time   | O(1) per op (O(k) for list_set_bits over k bits) |
| Space  | O(1)  |
Better Possible?
❌ No
Single-word bitwise instructions are already optimal for fixed-width flag sets.
'''
