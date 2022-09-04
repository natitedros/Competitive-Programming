class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        connections = defaultdict(list)
        for i,eq in enumerate(equations):
            d[(eq[0],eq[1])] = values[i]
            d[(eq[1],eq[0])] = 1/values[i]
            connections[eq[0]].append(eq[1])
            connections[eq[1]].append(eq[0])
        res = []
        for q in queries:
            if q[0] in connections and q[1] in connections:
                if q[0] == q[1]:
                    res.append(1)
                else:
                    visited = set()
                    queue = deque()
                    queue.append((q[0],1))
                    found = False
                    while queue:
                        numer,ans = queue.popleft()
                        visited.add(numer)
                        for denom in connections[numer]:
                            if denom not in visited:
                                if denom == q[1]:
                                    res.append(ans*d[(numer,denom)])
                                    found = True
                                    break
                                queue.append((denom,ans*d[(numer,denom)]))
                        if found:
                            break
                    if not found:
                        res.append(-1)
            else:
                res.append(-1)
        return res