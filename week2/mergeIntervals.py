class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        mergedArr = []
        for i in range(len(intervals)):
            if i == 0:
                mergedArr.append(intervals[i])
            else:
                if mergedArr[-1][1]>=intervals[i][0] and mergedArr[-1][1]<=intervals[i][1]:
                    mergedArr[-1][1] = intervals[i][1]
                elif mergedArr[-1][1]>=intervals[i][0] and mergedArr[-1][1]>=intervals[i][1]:
                    continue
                else:
                    mergedArr.append(intervals[i])
        return mergedArr