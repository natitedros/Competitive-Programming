class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        hp = sorted(arr)
        res = []
        count = l
        while hp:
            maxIndex = arr.index(hp.pop())
            res.append(maxIndex+1)
            arr = arr[maxIndex::-1] + arr[maxIndex+1::]
            res.append(count)
            arr = arr[count-1::-1] + arr[count::]
            count -= 1
        return res