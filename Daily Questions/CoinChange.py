class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque()
        visited = set()
        q.append((0,0))
        while q:
            val,level = q.popleft()
            if val == amount:
                return level
            elif val > amount:
                continue
            for coin in coins:
                if val+coin not in visited:
                    q.append((val+coin,level+1))
                    visited.add(val+coin)
        return -1