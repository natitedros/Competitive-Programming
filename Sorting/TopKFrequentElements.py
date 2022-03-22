class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        lst= sorted(freq.items(), key=lambda x:(x[1],x[0]), reverse = True)
        res=[]
        for i in range(k):
            res.append(lst[i][0])
        return res