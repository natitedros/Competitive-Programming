class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log[-1].isalpha():
                temp = log.split()
                temp = [temp[1:],temp[0]]
                letters.append(temp)
            else:
                digits.append(log)
        letters.sort()
        ans = []
        for let in letters:
            temp = [let[1]] + let[0]
            ans.append(" ".join(temp))
        ans += digits
        return ans