class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                if len(heap)<k:
                    heapq.heappush(heap,-1*(matrix[i][j]))
                else:
                    heapq.heappushpop(heap,-1*(matrix[i][j]))
        return -1*heap[0]