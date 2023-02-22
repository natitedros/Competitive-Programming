class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] = time[i]%60
        freq = {}
        count = 0
        for i in range(len(time)):
            comp = (60-time[i])%60
            if comp in freq:
                count += freq[comp]
            if time[i] not in freq:
                freq[time[i]] = 0
            freq[time[i]] += 1
        return count