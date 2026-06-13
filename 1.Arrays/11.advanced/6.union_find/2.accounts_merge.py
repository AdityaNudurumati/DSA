'''
2. Accounts Merge (Medium) — Union Find
Problem Statement

Each account is [name, email1, email2, ...]. Two accounts belong to the same person
if they share any email. Merge accounts: return [name, sorted unique emails...] per
person. (A name may repeat across different people.)

Example
Input:
accounts = [
  ["John","johnsmith@mail.com","john_newyork@mail.com"],
  ["John","johnsmith@mail.com","john00@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]

Output (order-independent):
[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
 ["Mary","mary@mail.com"],
 ["John","johnnybravo@mail.com"]]
'''

from collections import defaultdict

def accountsMerge(accounts):

    parent = {}             # email -> parent email
    owner = {}              # email -> account name

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    # union all emails within an account; record each email's owner name
    for acc in accounts:
        name = acc[0]
        first_email = acc[1]
        for email in acc[1:]:
            owner[email] = name
            union(first_email, email)

    # group emails by their representative root
    groups = defaultdict(list)
    for email in owner:
        groups[find(email)].append(email)

    result = []
    for root, emails in groups.items():
        result.append([owner[root]] + sorted(emails))

    return result


if __name__ == "__main__":
    out = accountsMerge([
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ])
    for group in sorted(out):
        print(group)
    # Expected (sorted):
    # ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
    # ['John', 'johnnybravo@mail.com']
    # ['Mary', 'mary@mail.com']

'''
Pattern
✅ Union-Find over emails

Key Observation
Treat emails as nodes; union all emails inside one account. Emails sharing a root
belong to the same person. Map each email to its owner name for the output.

| Metric | Value                  |
| ------ | ---------------------- |
| Time   | O(N α + N log N)       | (N = total emails; log from sorting)
| Space  | O(N)                   |

Better Possible?
DFS over an email graph works too; same complexity.
'''
