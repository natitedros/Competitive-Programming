class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [[ages[i],scores[i]] for i in range(len(scores))]
        arr.sort()
        dp = [arr[i][1] for i in range(len(arr))]
        for i,(mage, mscore) in enumerate(arr):
            for j in range(0,i):
                age, score = arr[j]
                if mscore >= score:
                    dp[i] = max(mscore+dp[j],dp[i])
        return max(dp)           
