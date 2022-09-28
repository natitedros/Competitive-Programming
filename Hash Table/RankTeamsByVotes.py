class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        d = {}
        for i in range(n):
            d[votes[0][i]] = [0]*n
        for vote in votes:
            for i,v in enumerate(vote):
                d[v][i] += 1
        arr = sorted(d.items(), key=lambda item: (item[1], ord('A')-ord(item[0])), reverse=True)
        res = []
        for char,freq in arr:
            res.append(char)
        return ''.join(res)
        