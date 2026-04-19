class Twitter:
    """

    userID --> list of (time, tweetID)
    userID --> set of followers
    -  O(1) follow and unfollow


    u1 --> set(u2, u3, u4)
    
    list 10 most recent tweets

    u1 --> [3, 7, 10]
    u2 --> [3, 6, 11]
    u3 --> [1, 5, 7]
    u4 --> [5, 4, 8]

    maxheap = [10, 7, 8, 6]

    res = [11, ]

    (-time, tweet, userID, index)

    """

    def __init__(self):
        # user to tweets
        self.user_to_tweets = defaultdict(list)
        self.user_to_following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # populate maxheap with initial end values
        maxh = []
        heapq.heapify(maxh)

        # set of users to get all list of tweets to merge
        users = {userId} | self.user_to_following[userId]
        for u in users:
            if self.user_to_tweets[u]:
                # (-time, tweet, userID, index)
                # get tweet list for each user, add last one to maxheap
                heapq.heappush(maxh, (
                    -self.user_to_tweets[u][-1][0], # -time
                    self.user_to_tweets[u][-1][1], # tweet
                    u, # userId
                    len(self.user_to_tweets[u])-1 # index
                ))
        
        # k-way merge w/ times, return res list
        res = []
        while maxh and len(res) < 10:
            time, tweet, userId, i = heapq.heappop(maxh)
            res.append(tweet)

            # add next elem to heap
            if i > 0:
                heapq.heappush(maxh, (
                    -self.user_to_tweets[userId][i-1][0],
                    self.user_to_tweets[userId][i-1][1],
                    userId,
                    i-1
                ))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].discard(followeeId)

