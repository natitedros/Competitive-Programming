class TweetCounts:

    def __init__(self):
        self.d = {}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.d:
            self.d[tweetName] = []
        self.d[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        size = (endTime - startTime) // 86400 + 1
        sec = 86400
        if freq == "minute":
            size = (endTime - startTime) // 60 + 1
            sec = 60
        elif freq == "hour":
            size = (endTime - startTime) // 3600 + 1
            sec = 3600
        res = [0]*size
        for time in self.d[tweetName]:
            if startTime <= time <= endTime:
                ind = int((time-startTime)/sec)
                res[ind] += 1
        return res
        
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)