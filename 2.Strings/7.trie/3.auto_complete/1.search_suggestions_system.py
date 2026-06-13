'''
1. Search Suggestions System (Medium)
Problem Statement

Given an array products and a string searchWord, after each character typed of
searchWord return up to 3 product names that share the typed prefix. Suggestions
must be the lexicographically smallest 3, returned in sorted order.

Example
Input:
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

Output:
[["mobile","moneypot","monitor"],
 ["mobile","moneypot","monitor"],
 ["mouse","mousepad"],
 ["mouse","mousepad"],
 ["mouse","mousepad"]]
'''

def suggestedProducts(products, searchWord):

    # Build a trie; at each node keep the (sorted, capped-at-3) suggestions so a
    # lookup is just a walk down the prefix with no extra sorting per query.
    root = {}
    for product in sorted(products):          # insert in sorted order
        node = root
        for ch in product:
            node = node.setdefault(ch, {'sug': []})
            if len(node['sug']) < 3:          # keep only the first 3 (smallest)
                node['sug'].append(product)

    result = []
    node = root
    fell_off = False
    for ch in searchWord:
        if not fell_off and ch in node:
            node = node[ch]
            result.append(node['sug'])
        else:
            # prefix no longer exists in the trie -> no more suggestions
            fell_off = True
            result.append([])

    return result


if __name__ == "__main__":
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))
    # Expected: [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]

'''
Pattern
✅ Trie + precomputed suggestions — insert products sorted, cache the top-3 at every
   node, so each keystroke answers in O(1) per prefix character.

| Metric | Value                                                  |
| ------ | ------------------------------------------------------ |
| Time   | O(S log S) sort + O(S) build, O(len(searchWord)) query |
| Space  | O(S) where S = total product characters                |

Better Possible?
A simpler approach sorts once and binary-searches the prefix range per keystroke in
O(S log S + Q·log S). The trie trades extra space for faster repeated prefix queries.
'''
