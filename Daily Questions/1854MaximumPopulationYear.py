class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        maxVal = 0
        for i in range(100):
            for start, end in logs:
                if start <= i+1950 < end:
                    d[i+1950] += 1
                    maxVal = max(maxVal, d[i+1950])
        for i in range(100):
            if d[i+1950] == maxVal:
                return i+1950