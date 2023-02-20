class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counter = [Counter(sticker) for sticker in stickers] 
        n = len(counter)
        @lru_cache(None)
        def dfs(target):
            if not target: return 0
            targ_counter = Counter(target)
            res = float('inf')
            for i in range(n):
                if counter[i][target[0]] == 0:
                    continue
                s = ''
                for j in range(26):
                    char = chr(j+97)
                    s += char*max(targ_counter[char] - counter[i][char], 0)
                if dfs(s) != -1:
                    res = min(res, 1 + dfs(s))
            if res == float('inf'):
                return -1
            return res
        return dfs(target)