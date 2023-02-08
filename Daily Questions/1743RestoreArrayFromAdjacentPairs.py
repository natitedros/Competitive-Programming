class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neigh = defaultdict(set)
        for u, v in adjacentPairs:
            neigh[u].add(v)
            neigh[v].add(u)
            
        res = []
        def rec(key, parent):
            res.append(key)
            for val in neigh[key].values():
                if val != parent:
                    neigh[val].remove(key)
                    rec(val, key)

        for key in neigh.keys():
            if len(neigh[key]) == 1:
                rec(key, 1000000)
                break
        return res