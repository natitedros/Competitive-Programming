class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strDict = {}
        counterDict = {}
        for i in range(len(nums)):
            a = str(nums[i])*15
            a = int(a[:15])
            if nums[i] in strDict:
                strDict[nums[i]].append(a)
                counterDict[nums[i]] += 1
            else:
                strDict[nums[i]] = [a]
                counterDict[nums[i]] = 1
        
        strDict = sorted(strDict, key = lambda x : strDict[x][0], reverse = True)
        res = []
        print(strDict)
        for key in strDict:
            if strDict == [0]:
                res.append(str(key))
            else:
                for i in range(counterDict[key]):
                    res.append(str(key))
        
        res = ''.join(res)
        return res