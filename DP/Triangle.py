class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        d = {}
        def minPath(ind, length):
            if length > l:
                return 0
            if (ind,length) not in d:
                d[(ind,length)] = triangle[length-1][ind] + min(minPath(ind,length+1), minPath(ind+1,length+1))
            return d[(ind,length)]
        return minPath(0, 1)