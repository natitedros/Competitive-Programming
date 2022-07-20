class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        l = len(nums)
        visited = set()
        res = 0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    vis = [nums[i],nums[j],nums[k]]
                    if tuple(vis) in visited:
                        continue
                    sm = sum(vis)
                    for m in range(k+1,l):
                        if sm == nums[m]:
                            res += 1
        return res