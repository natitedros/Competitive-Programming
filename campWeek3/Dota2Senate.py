class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        q = deque()
        for i in range(n):
            q.append(senate[i])
        deletedD = 0
        deletedR = 0
        while "D" in q and "R" in q:
            temp = q.popleft()
            if temp == "R" and deletedR == 0:
                deletedD += 1
                q.append(temp)
            elif temp == "R":
                deletedR -= 1
            elif temp == "D" and deletedD == 0:
                deletedR += 1
                q.append(temp)
            elif temp == "D":
                deletedD -= 1
        if "D" not in q:
            return "Radiant"
        return "Dire"