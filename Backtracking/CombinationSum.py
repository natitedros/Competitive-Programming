class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def dfs(ind,sm,comb):
            if sm > target:
                return
            if sm == target:
                res.append(comb.copy())
                return
            for i in range(ind,n):
                comb.append(candidates[i])
                dfs(i,sm+candidates[i],comb)
                comb.pop()
        dfs(0,0,[])
        return res