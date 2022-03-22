class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.arr = []
        for i in range(len(nums)):
            if len(self.arr)<self.k:
                heapq.heappush(self.arr,nums[i])
            else:
                heapq.heappushpop(self.arr,nums[i])
        
    def add(self, val: int) -> int:
        if len(self.arr)<self.k:
            heapq.heappush(self.arr,val)
        else:
            heapq.heappushpop(self.arr,val)
        return (self.arr[0])
