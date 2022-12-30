class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        #sort the queries
        #queue for bfs
        #move right or down
        #start queue from smallest query and go bfs until the possible path
        #hold previous answer as cumulative and start from that for the next query
        #visited set
        ans = defaultdict(int)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def isInbound(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        sortedQuery = sorted(queries, reverse = True)
        queue = []
        visited = set()
        visited.add((0,0))
        heapq.heappush(queue, (grid[0][0], 0, 0))
        acc = 0
        while queue:
            if sortedQuery and queue[0][0] >= sortedQuery[-1]:
                ans[sortedQuery[-1]] = acc
                sortedQuery.pop()
            elif sortedQuery:
                val, row, col = heapq.heappop(queue)
                acc += 1
                for r, c in dirs:
                    newr = row+r
                    newc = col+c
                    if isInbound(newr, newc) and (newr, newc) not in visited:
                        visited.add((newr, newc))
                        heapq.heappush(queue, (grid[newr][newc], newr, newc))
            else:
                queue = None
        while sortedQuery:
            ans[sortedQuery[-1]] = acc
            sortedQuery.pop()
        result = []
        for q in queries:
            result.append(ans[q])
        return result
                
            