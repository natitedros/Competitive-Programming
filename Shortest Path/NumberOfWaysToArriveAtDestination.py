class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for int1, int2, time in roads:
            neighbors[int1].append((time, int2))
            neighbors[int2].append((time, int1))
            
        queue = list()
        queue.append((0, 0))
        reachingTime = [inf]*n
        reachingTime[0] = 0
        ways = [0]*n
        ways[0] = 1
        mod = (10**9)+7
        while queue:
            time, vertex = heapq.heappop(queue)
            if vertex == n-1:
                return ways[vertex] % mod
            for curr_time, neigh in neighbors[vertex]:
                if time+curr_time < reachingTime[neigh]:
                    reachingTime[neigh] = time+curr_time
                    ways[neigh] = ways[vertex]
                    heapq.heappush(queue, (time+curr_time, neigh))
                elif time+curr_time == reachingTime[neigh]:
                    ways[neigh] += ways[vertex]
