class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        prev = defaultdict(int)
        deleted = set()
        for char in words[0]:
            prev[char] += 1
        for i in range(1,n):
            temp = defaultdict(int)
            for char in words[i]:
                temp[char] += 1
            if temp == prev:
                deleted.add(i)
            prev = temp
        res = []
        for i in range(n):
            if i not in deleted:
                res.append(words[i])
        return res