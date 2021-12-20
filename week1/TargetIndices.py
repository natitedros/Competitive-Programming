class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        freq = [0]*101
        for i in nums:
            freq[i]+=1
        sortedArr = []
        for i in range(len(freq)):
            if freq[i] != 0:
                for j in range(freq[i]):
                    sortedArr.append(i)
        arr = []
        for i in range(len(sortedArr)):
            if sortedArr[i]==target:
                arr.append(i)
        return arr
