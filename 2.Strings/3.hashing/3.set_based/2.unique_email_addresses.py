'''
2. Unique Email Addresses (Easy)
Problem Statement

Every email has a local name and a domain name separated by '@'. In the local
name: '.' characters are ignored, and everything after a '+' is ignored. The
domain name is used as-is. Return the number of distinct addresses that actually
receive mail.

Example
Input:
emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]

Output:
2
'''

def numUniqueEmails(emails):

    unique = set()

    for email in emails:
        local, domain = email.split('@')
        # drop everything from the first '+' onward
        local = local.split('+')[0]
        # remove all dots from the local part
        local = local.replace('.', '')
        unique.add(local + '@' + domain)

    return len(unique)


if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com",
              "testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails))   # Expected: 2

'''
Pattern
✅ Set Based (canonicalize then dedup)

Key Observation
Normalize each address to its canonical delivery form (strip dots and the
'+suffix' in the local part) and add it to a set; the set size is the answer.

| Metric | Value |
| ------ | ----- |
| Time   | O(n * k) |
| Space  | O(n * k) |

Better Possible?
Optimal — each character of each email is processed once. n = number of emails,
k = average email length.
'''
