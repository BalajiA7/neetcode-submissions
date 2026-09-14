class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append([self.count, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        latestPosts = []
        # add the current user
        self.follows[userId].add(userId)

        for followerId in self.follows[userId]:
            index = len(self.tweets[followerId]) -1
            if index >=0:
                count, postId = self.tweets[followerId][index]
                heapq.heappush(latestPosts, [count, postId,followerId, index-1])

        res = []
        while len(latestPosts) and len(res) < 10:
            count, postId, followerId, index = heapq.heappop(latestPosts)
            res.append(postId)
            if index >= 0:
                nextCount, nextPostId = self.tweets[followerId][index]
                heapq.heappush(latestPosts, [nextCount, nextPostId, followerId, index-1])
        
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
