class Twitter:

    def __init__(self):
        self.posts = 0
        self.userPosts = defaultdict(list)
        self.userFollows = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts+=1
        self.userPosts[userId].append([self.posts,tweetId])
        self.userFollows[userId].add(userId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        recentPosts = []
        heap = []
        for followerId in self.userFollows[userId]:
            tweets = self.userPosts[followerId]
            for idx,tweetId in tweets:
                heap.append([-idx,tweetId])
        heapq.heapify(heap)


        while heap and len(recentPosts) < 10:
            idx,latestTweetId = heapq.heappop(heap)
            recentPosts.append(latestTweetId)
        
        return recentPosts
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        
