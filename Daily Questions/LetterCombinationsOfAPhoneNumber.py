class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {}
        d['2'] = ['a','b','c']
        d['3'] = ['d','e','f']
        d['4'] = ['g','h','i']
        d['5'] = ['j','k','l']
        d['6'] = ['m','n','o']
        d['7'] = ['p','q','r','s']
        d['8'] = ['t','u','v']
        d['9'] = ['w','x','y','z']
        def possibleCombos(one, two):
            arr = []
            for i in range(len(two)):
                for j in range(len(one)):
                    arr.append(one[j]+two[i])
            return arr
        l = len(digits)
        res=[]
        if l > 0:
            res = [""]
        for i in range(l):
            res = possibleCombos(res, d[digits[i]])
        return res