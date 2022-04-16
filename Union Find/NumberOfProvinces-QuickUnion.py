class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [0]*n
        rank = [1]*n
        joined = set()
        for i in range(n):
            parent[i] = i
        def find(city):
            if city == parent[city]:
                return city
            return find(parent[city])
        def union(one, two):
            parentOne = find(one)
            parentTwo = find(two)
            if parentOne == parentTwo:
                return 0
            if rank[parentOne] > rank[parentTwo]:
                parent[parentTwo] = parentOne
            elif rank[parentTwo] > rank[parentOne]:
                parent[parentOne] = parentTwo
            else:
                parent[parentTwo] = parentOne
                rank[parentOne] += 1
        for i in range(n):
            for j in range(n):
                if i != j and (i,j) not in joined and isConnected[i][j] == 1:
                    joined.add((j,i))
                    union(i, j)
        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1
        return count