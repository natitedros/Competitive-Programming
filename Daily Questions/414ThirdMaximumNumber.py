class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNum = set()
        heap = []
        for num in nums:
            if num not in setNum:
                setNum.add(num)
                heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)
        if len(heap) == 3:
            return heap[0]
        return max(heap)