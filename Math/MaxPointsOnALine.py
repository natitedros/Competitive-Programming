class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        line = defaultdict(set)
        for i in range(1, len(points)):
            for j in range(i):
                if not points[i][0] - points[j][0]:
                    slope = inf
                    yInt = inf
                    xInt = points[i][0]
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    yInt = (slope*points[i][0]) - points[i][1]
                    if not slope:
                        xInt = inf
                    else:
                        xInt = yInt/slope
                line[(slope, yInt, xInt)].add((points[i][0], points[i][1]))
                line[(slope, yInt, xInt)].add((points[j][0], points[j][1]))
        result = 0
        for vals in line.values():
            result = max(result, len(vals))
        return result
        