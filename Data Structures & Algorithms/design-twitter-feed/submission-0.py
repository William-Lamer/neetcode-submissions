class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # user -> [(time, tweetId)]
        self.following = defaultdict(set) # user -> {userIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following[userId] | {userId}
        heap = []

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]
                heap.append((-time, tweetId, u, idx))
        heapq.heapify(heap)

        feed = []
        while heap and len(feed) < 10:
            _, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                time, newTweetId = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-time, newTweetId, u, idx -1))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
