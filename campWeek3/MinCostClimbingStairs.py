class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dicts = {}
        def steps(i):
            if i>=len(cost):
                return 0
            if i in dicts:
                return dicts[i]
            temp = cost[i]+min(steps(i+1),steps(i+2))
            dicts[i] = temp
            return temp
        return min(steps(0),steps(1))