class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        l = len(points)
        current = 0
        overlapping = 0
        res = 0
        while current < l:
            right = points[current][1]
            while overlapping < l and right >= points[overlapping][0]:
                right = min(right, points[overlapping][1])
                overlapping += 1
            current = overlapping
            overlapping += 1
            res += 1
        return res