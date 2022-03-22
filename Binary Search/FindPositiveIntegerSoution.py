class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        arr = []
        for i in range(1,z+1):
            arr.append(i)
        res = []
        for i in range(z):
            left = 0
            right = z-1
            while left <= right:
                mid = left + (right-left)//2
                if customfunction.f(arr[i], arr[mid]) < z:
                    left = mid+1
                elif customfunction.f(arr[i],arr[mid]) > z:
                    right = mid-1
                else:
                    res.append([arr[i],arr[mid]])
                    break
        return res