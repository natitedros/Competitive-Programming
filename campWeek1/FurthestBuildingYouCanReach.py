class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        sumBricks = 0
        i = 0
        n = len(heights)
        while sumBricks <= bricks and i<n-1:
            i += 1
            if len(heap)<ladders:
                if heights[i-1]<heights[i]:
                    heapq.heappush(heap, heights[i]-heights[i-1])
            else:
                if heights[i-1]<heights[i]:
                    sumBricks += heapq.heappushpop(heap, heights[i]-heights[i-1])
        if sumBricks <= bricks:
            return i
        return i-1