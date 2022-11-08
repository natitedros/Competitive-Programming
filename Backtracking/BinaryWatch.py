# Backtracking
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        time = [8,4,2,1,32,16,8,4,2,1]
        n = len(time)
        res = []
        def backtrack(ind,hr,mint,leds):
            if not leds:
                temp = str(mint)
                if mint//10 == 0:
                    temp = "0"+temp
                res.append(str(hr)+":"+temp)
                return
            for i in range(ind+1,n-leds+1):
                if 0<=i<4 and hr+time[i] <= 11:
                    backtrack(i,hr+time[i],mint,leds-1)
                elif i>=4 and mint+time[i] <= 59:
                    backtrack(i,hr,mint+time[i],leds-1)
        backtrack(-1,0,0,turnedOn)
        return res
# Bit manipulation
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    minute = str(m)
                    if int(minute) // 10 == 0:
                        minute = "0" + minute
                    result.append(str(h) + ":" + minute)
        return result