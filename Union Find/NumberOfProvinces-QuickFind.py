class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [0]*n
        province = {}
        joined = set()
        for i in range(n):
            parent[i] = i
            province[i] = [i]
        def find(city):
            return parent[city]
        def union(one, two):
            parentOne = find(one)
            parentTwo = find(two)
            if parentOne == parentTwo:
                return 0
            if len(province[parentTwo]) > len(province[parentOne]):
                parentTwo, parentOne = parentOne, parentTwo
            for i in range(len(province[parentTwo])):
                parent[province[parentTwo][i]] = parentOne
                province[parentOne].append(province[parentTwo][i])
            del province[parentTwo]
        for i in range(n):
            for j in range(n):
                if i != j and (i,j) not in joined and isConnected[i][j] == 1:
                    joined.add((j,i))
                    union(i, j)
        return len(province)