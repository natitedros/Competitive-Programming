class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        stk = []
        for i in range(n):
            while stk and height[stk[-1][1]] < height[i]:
                res += (min(height[stk[-1][0]],height[i])-height[stk[-1][1]])*(i-stk[-1][0]-1)
                stk.pop()
            if stk:
                if height[stk[-1][1]] == height[i]:
                    stk[-1][1] = i
                else:
                    stk.append([stk[-1][1],i])
            else:
                stk.append([i,i])
        return res