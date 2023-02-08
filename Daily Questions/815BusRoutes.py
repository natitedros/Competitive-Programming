class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        queue = deque()
        for i in range(len(routes)):
            routes[i] = set(routes[i])
        visited = set()
        for i in range(len(routes)):
            if source in routes[i]:
                queue.append([routes[i],source])
                visited.add(i)
        buses = 1
        while queue:
            length = len(queue)
            for _ in range(length):
                route, prev = queue.popleft()
                if target in route:
                    return buses
                for val in route:
                    if val != route:
                        for i in range(len(routes)):
                            if i not in visited and val in routes[i]:
                                queue.append([routes[i], val])
                                visited.add(i)
            buses += 1
        return -1
