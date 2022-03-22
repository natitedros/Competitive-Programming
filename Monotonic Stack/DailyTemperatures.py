class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        t = []
        for i in range(0,len(temperatures)):  
            t.append([temperatures[i],0])
        for i in range(len(temperatures)):
            if stack == []:
                stack.append(i)
            else:
                while stack != [] and temperatures[i]>temperatures[stack[-1]]:
                    temp = stack.pop()
                    t[temp][1] = i-temp
                stack.append(i)
        res = []
        for i in range(len(t)):
            res.append(t[i][1])
        return res