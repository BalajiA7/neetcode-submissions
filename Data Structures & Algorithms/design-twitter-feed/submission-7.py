class Twitter:

    def __init__(self):
        self.posts = 1
        self.userPosts = defaultdict(list)
        self.userFollows = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append([self.posts,tweetId])
        self.posts-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        recentPosts = []
        heap = []
        self.userFollows[userId].add(userId)

        for followeeId in self.userFollows[userId]:
            tweets = self.userPosts[followeeId]
            # instead of adding all tweets to heap just add last for all followeeId
            index = len(tweets)-1
            if index >= 0:
                count,tweetId = self.userPosts[followeeId][index]
                # keep an reference for the next index reference as well
                heapq.heappush(heap, [count,tweetId,followeeId,index-1])

        while heap and len(recentPosts) < 10:
            count,tweetId,followeeId,index = heapq.heappop(heap)
            recentPosts.append(tweetId)
            # push the previous index into heap for the current followeeId
            tweets = self.userPosts[followeeId]
            if index >= 0:
                count,tweetId = self.userPosts[followeeId][index]
                heapq.heappush(heap, [count,tweetId,followeeId,index-1])
        
        return recentPosts
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        
