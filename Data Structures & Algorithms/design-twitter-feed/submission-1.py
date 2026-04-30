class Twitter:

    def __init__(self):
        self.following = collections.defaultdict(set) # user: followings
        self.tweets = collections.defaultdict(list) # user: (time, tweet_id)
        self.time = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.following[userId].add(userId)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.following[userId]
        timeline = []
        for follow in followings:
            timeline.extend(self.tweets[follow])
        size = min(10, len(timeline))
        return [tweet for (_, tweet) in sorted(timeline)[:size]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
        
