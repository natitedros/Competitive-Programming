class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        n = len(timePoints)
        minSmall = inf
        for i in range(1,n):
            hr = int(timePoints[i][:2]) - int(timePoints[i-1][:2])
            mnt = int(timePoints[i][3:]) - int(timePoints[i-1][3:])
            if hr > 12:
                hr = 24-hr
                mnt *= -1
            minSmall = min(minSmall,(hr*60)+mnt)
        hr = int(timePoints[n-1][:2]) - int(timePoints[0][:2])
        mnt = int(timePoints[n-1][3:]) - int(timePoints[0][3:])
        if hr > 12:
            hr = 24-hr
            mnt *= -1
        minSmall = min(minSmall,(hr*60)+mnt)
        return minSmall