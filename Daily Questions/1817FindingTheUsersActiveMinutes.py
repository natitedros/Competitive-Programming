class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)
        for user, time in logs:
            UAM[user].add(time)
        count = defaultdict(list)
        for key in UAM.keys():
            count[len(UAM[key])].append(key)
        res = [0]*k
        for i in range(k):
            res[i] = len(count[i+1])
        return res