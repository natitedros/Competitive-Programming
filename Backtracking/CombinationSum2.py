class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        visited = set()
        n,res = len(candidates),[]
        def dfs(ind,sm,comb):
            if sm > target:
                return
            if sm == target:
                temp = tuple(comb)
                res.append(temp)
                return
            done = set()
            for i in range(ind+1,n):
                if candidates[i] not in done:
                    done.add(candidates[i])
                    comb.append(candidates[i])
                    dfs(i,sm+candidates[i],comb)
                    comb.pop()
        dfs(-1,0,[])
        return res