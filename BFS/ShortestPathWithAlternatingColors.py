class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        outgoingRed = defaultdict(list)
        outgoingBlue = defaultdict(list)
        for curr_node, next_node in redEdges:
            outgoingRed[curr_node].append(next_node)
        for curr_node, next_node in blueEdges:
            outgoingBlue[curr_node].append(next_node)
            
        answer = []
        for node in range(n):
            startRed = self.bfs(0,node,True,outgoingRed,outgoingBlue)
            startBlue = self.bfs(0,node,False,outgoingRed,outgoingBlue)
            res = min(startRed,startBlue)
            if res == inf:
                answer.append(-1)
            else:
                answer.append(res)
            
        return answer
        
    def bfs(self,start, end, isRed, outgoingRed, outgoingBlue):
        step = 0
        queue = deque([(start,isRed)])
        visited = set()
        while queue:
            length = len(queue)
            while length:
                length -= 1
                current, isRed = queue.popleft()
                if (current, isRed) not in visited:
                    visited.add((current,isRed))
                    if current == end:
                        return step
                    if isRed:
                        for node in outgoingRed[current]:
                            queue.append((node,not isRed))
                    else:
                        for node in outgoingBlue[current]:
                            queue.append((node,not isRed))
            step += 1
        return inf            
