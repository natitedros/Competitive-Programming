class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        temp = date.split()
        year = temp.pop()
        mon = str(month[temp.pop()])
        day = temp.pop()[:-2]
        if len(mon) == 1:
            mon = "0"+mon
        if len(day) == 1:
            day = "0"+day
        ans = [year,mon,day]
        return "-".join(ans)