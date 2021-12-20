class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            arr = []
            for j in range(l[i], r[i]+1,1):
                arr.append(nums[j])
            arr.sort()
            arith = False
            if len(arr) == 2:
                arith = True
                res.append(arith)
            else:
                for k in range(1,len(arr)-1):
                    if arr[k]-arr[k-1] == arr[k+1]-arr[k]:
                        arith = True
                    else:
                        arith = False
                        break
                res.append(arith)
        return res