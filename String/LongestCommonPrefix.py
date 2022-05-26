class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        if l == 0:
            return ""
        res = list(strs[0])
        lenRes = len(res)
        for i in range(1,l):
            lenRes = min(lenRes,len(strs[i]))
            for j in range(lenRes):
                if res[j] != strs[i][j]:
                    lenRes = j
                    break
        return ''.join(res[:lenRes])
        