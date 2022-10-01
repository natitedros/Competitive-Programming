class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        res = []
        def rec(ind,sentence):
            if ind == n:
                res.append(" ".join(sentence))
                return 
            word = ""
            for i in range(ind,n):
                word += s[i]
                if word in wordDict:
                    sentence.append(word)
                    rec(i+1,sentence)
                    sentence.pop()
        rec(0,[])
        return res