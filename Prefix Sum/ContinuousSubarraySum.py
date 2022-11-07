class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        index =  {0: -1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix = (prefix + num)%k
            if prefix in index:
                if i - index[prefix] > 1:
                    return True
            else:
                index[prefix] = i
        return False
