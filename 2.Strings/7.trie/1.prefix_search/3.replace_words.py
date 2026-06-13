'''
3. Replace Words (Medium)
Problem Statement

You are given a list of roots and a sentence. If a word in the sentence has a
root as a prefix, replace the word with that root. If a word can be matched by
several roots, use the SHORTEST one. Words with no matching root stay unchanged.

Example
Input:
roots = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

Output:
"the cat was rat by the bat"
'''

def replaceWords(roots, sentence):

    # Build a trie of the roots.
    root = {}
    for word in roots:
        node = root
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True  # marks the end of a complete root

    def shortest_root(word):
        # Walk the word through the trie; stop at the FIRST root end we hit,
        # which is guaranteed to be the shortest matching root.
        node = root
        prefix = []
        for ch in word:
            if ch not in node:
                break
            prefix.append(ch)
            node = node[ch]
            if '#' in node:
                return "".join(prefix)
        return word  # no root matched -> keep the original word

    return " ".join(shortest_root(w) for w in sentence.split())


if __name__ == "__main__":
    roots = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replaceWords(roots, sentence))  # Expected: the cat was rat by the bat

'''
Pattern
✅ Trie of roots + early stop — descend each word until the first end-of-root marker
   gives the shortest root prefix automatically.

| Metric | Value                                          |
| ------ | ---------------------------------------------- |
| Time   | O(R + W) build R roots, scan W sentence chars  |
| Space  | O(R) for the trie                              |

Better Possible?
A hash set of roots with per-word prefix probing also works but you must test every
prefix length of each word. The trie checks all roots in a single descent, so it is
the natural optimum here.
'''
