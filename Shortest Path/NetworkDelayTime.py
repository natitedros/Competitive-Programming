#Bellman Ford
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minTime = [inf]*(n+1)
        minTime[k] = 0
        minTime[0] = 0
        for _ in range(n):
            tempArray = minTime.copy()
            for start, end, time in times:
                if minTime[start]+time < tempArray[end]:
                    tempArray[end] = minTime[start]+time
            minTime = tempArray
        answer = max(minTime)
        if answer == inf:
            return -1
        return answer

# Dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        outgoing = [[] for _ in range(n+1)]
        for u,v,w in times:
            outgoing[u].append([v,w])
        minTime = 0
        heap = []
        visited = set()
        
        heapq.heappush(heap,(0,k))
        while heap:
            curr_time,curr_node = heapq.heappop(heap)
            if curr_node not in visited:
                visited.add(curr_node)
                minTime = curr_time
                # minTime = max(minTime,curr_time)
                for neighbour,time in outgoing[curr_node]:
                    if neighbour not in visited:
                        heapq.heappush(heap,(curr_time+time,neighbour))
            
        if len(visited) != n:
            return -1
        return minTime