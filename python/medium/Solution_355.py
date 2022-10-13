# 355. Design Twitter

from typing import List
import collections
import itertools
import heapq


class Twitter:
    def __init__(self):
        self.timer = itertools.count()
        self.posts = collections.defaultdict(collections.deque)
        self.follows = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((-next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        target = self.follows[userId] | {userId}
        posts = (self.posts[user] for user in self.posts if user in target)
        tweets = itertools.islice(heapq.merge(*posts), 10)
        return [tweet[1] for tweet in tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
param_2 = obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
param_3 = obj.getNewsFeed(1)
obj.unfollow(1, 2)
param_4 = obj.getNewsFeed(1)
print(f'{param_2=} {param_3=} {param_4=}')
