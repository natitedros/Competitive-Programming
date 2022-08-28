class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i in range(len(tickets)):
            q.append(i)
        res = 0
        while q:
            ind = q.popleft()
            tickets[ind] -= 1
            res += 1
            if ind == k and not tickets[ind]:
                return res
            if tickets[ind]:
                q.append(ind)