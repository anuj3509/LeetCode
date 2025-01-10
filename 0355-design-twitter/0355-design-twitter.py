class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)   # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)   # userId -> set of followeeId        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1     # this will be then used in the min heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []    # ordered startig from recent tweets from all the people this person follows
        minHeap = []

        self.followMap[userId].add(userId)      # because the user also follows himself
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1  # to get the last index
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        #         minHeap.append([count, tweetId, followeeId, index - 1])     # index - 1 indicates the next position we will be looking for
        # heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
           count, tweetId, followeeId, index = heapq.heappop(minHeap)
           res.append(tweetId)

           # checks if the same person has some more tweets let which we haven't added yet
           if index >= 0:   
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)