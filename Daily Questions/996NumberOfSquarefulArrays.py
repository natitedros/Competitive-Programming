class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def rec(freq,path,res):
            if freq=={}:  
                res.append(path)
                return 
            for i in list(freq.keys()):
                if path==[]:
                    if freq[i]==1:
                        del freq[i]
                    else:
                        freq[i]-=1
                    rec(freq,path+[i],res)
                    freq[i]+=1
                else:
                    if freq[i]==1:
                        del freq[i]
                    else:
                        freq[i]-=1
                    if int((i+path[-1])**(0.5))**2 == i + path[-1]:
                        rec(freq,path+[i],res)
                    freq[i]+=1
        path=[]
        res=[]
        freq = Counter(nums)
        rec(freq,path,res)
        return len(res)