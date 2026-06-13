'''
355. Design Twitter (Hard)
Problem Statement

Design a simplified Twitter where users can post tweets, follow / unfollow other
users, and see the 10 most recent tweets in their news feed.

Implement the Twitter class:
- postTweet(userId, tweetId)  : compose a new tweet.
- getNewsFeed(userId)         : return the 10 most recent tweet ids posted by the
                                user or by users they follow, newest first.
- follow(followerId, followeeId)
- unfollow(followerId, followeeId)

Example:
Input:
postTweet(1, 5); getNewsFeed(1); follow(1, 2); postTweet(2, 6);
getNewsFeed(1); unfollow(1, 2); getNewsFeed(1)
Output:
[5]
[6, 5]
[5]
'''

import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0                       # global monotonic clock for ordering
        self.tweets = defaultdict(list)     # userId -> list of (time, tweetId)
        self.following = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        # record tweet with an ever-increasing timestamp
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        # candidate authors: the user themselves + everyone they follow
        authors = self.following[userId] | {userId}

        # max-heap by time: push the latest tweet of each author as (-time, idx, author)
        heap = []
        for author in authors:
            tweets = self.tweets[author]
            if tweets:
                idx = len(tweets) - 1               # newest tweet of this author
                t, tid = tweets[idx]
                heapq.heappush(heap, (-t, idx, author))

        feed = []
        # pop the globally newest tweet, then refill from that same author
        while heap and len(feed) < 10:
            neg_t, idx, author = heapq.heappop(heap)
            feed.append(self.tweets[author][idx][1])
            if idx > 0:                             # older tweet from same author
                prev_idx = idx - 1
                t, tid = self.tweets[author][prev_idx]
                heapq.heappush(heap, (-t, prev_idx, author))
        return feed

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)


if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))   # Expected: [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))   # Expected: [6, 5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))   # Expected: [5]


'''
Pattern
✅ Design + K-Way Merge with a Heap
Each author's tweets are already in time order, so finding the 10 newest across
N authors is a k-way merge: seed a max-heap with each author's latest tweet, pop
the newest, then refill from that author's next-older tweet. A global timestamp
gives a total ordering so tweets from different authors interleave correctly.

| Metric | Value |
| ------ | -------------------------------------- |
| Time   | postTweet O(1), getNewsFeed O(N log N)  |
| Space  | O(U + T) users + tweets, heap O(N)      |

N = number of authors followed (+self), U = users, T = total tweets.

Better Possible?
❌ Not asymptotically for getNewsFeed under this model — we must consider every
followee's latest tweet at least once, so O(N) work is unavoidable, and the heap
adds only a log factor while bounding work to the 10 needed. A counter id instead
of a clock would work equally well.
'''
