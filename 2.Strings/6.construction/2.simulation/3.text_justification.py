'''
3. Text Justification (Hard)
Problem Statement

Given an array of words and a width maxWidth, format the text so that each
line has exactly maxWidth characters and is fully (left and right) justified.

Pack as many words as fit on a line (words separated by at least one space).
Distribute extra spaces as evenly as possible; if spaces don't divide evenly,
the left slots get more spaces than the right. The last line is left-justified
(single spaces between words) and padded with trailing spaces. A line with a
single word is also left-justified.

Example
Input:
words = ["This","is","an","example","of","text","justification."]
maxWidth = 16

Output:
["This    is    an", "example  of text", "justification.  "]
'''

def fullJustify(words, maxWidth):
    res = []
    line = []          # words on the current line
    line_len = 0       # total length of those words (no spaces yet)

    for w in words:
        # +len(line) accounts for the minimum one space between words
        if line_len + len(w) + len(line) > maxWidth:
            # flush the current line, fully justified
            spaces = maxWidth - line_len
            if len(line) == 1:
                res.append(line[0] + ' ' * spaces)  # single word: left-justify
            else:
                gaps = len(line) - 1
                even, extra = divmod(spaces, gaps)  # leftmost gaps get the extra
                built = []
                for k, word in enumerate(line):
                    built.append(word)
                    if k < gaps:
                        built.append(' ' * (even + (1 if k < extra else 0)))
                res.append(''.join(built))
            line = []
            line_len = 0

        line.append(w)
        line_len += len(w)

    # last line: left-justified, single spaces, pad the end
    last = ' '.join(line)
    res.append(last + ' ' * (maxWidth - len(last)))
    return res


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(fullJustify(words, 16))
    # Expected: ['This    is    an', 'example  of text', 'justification.  ']


'''
Pattern
✅ Simulation (greedy line packing + careful space distribution)
Greedily fit words per line, then for each completed line spread the leftover
spaces evenly (left gaps get the remainder); the final line is left-justified.

| Metric | Value                        |
| ------ | ---------------------------- |
| Time   | O(total characters)          |
| Space  | O(total characters) output   |

Better Possible?
❌ No — output size is the lower bound; this is a single pass.
'''
