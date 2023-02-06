class Solution:
    def differByOne(self, word1, word2):
        ptr1, ptr2 = 0, 0
        turn = 1
        while ptr1 < len(word1) and ptr2 < len(word2) and turn >= 0:
            if word1[ptr1] != word2[ptr2]:
                turn -= 1
                ptr1 -= 1
            ptr1 += 1
            ptr2 += 1
        return turn >= 0

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        def rec(ind, prev):
            if (ind, prev) in dp:
                return dp[(ind, prev)]
            if ind == len(words) or len(words[ind]) - len(words[prev]) > 1:
                return 0
            dp[(ind, prev)] = rec(ind+1, prev)
            if prev == -1 or (len(words[ind]) == len(words[prev]) + 1 and self.differByOne(words[prev], words[ind])):
                dp[(ind, prev)] = max(dp[(ind, prev)], 1 + rec(ind+1, ind))
            return dp[(ind, prev)]
        ans = rec(0, -1)
        return ans
     