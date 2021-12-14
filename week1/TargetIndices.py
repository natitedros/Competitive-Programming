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
<<<<<<< HEAD
        return arr
=======
        return arr
>>>>>>> 0b66944f25ff706de81f5bb264ed5ec904798bcf
