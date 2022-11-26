class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        root = None
        tree = defaultdict(list)
        for node in range(len(parent)):
            if parent[node] == -1:
                root = node
            else:
                tree[parent[node]].append(node)
            result = 1
            def dfs(node):
                nonlocal result
                max1 = 0
                max2 = 0
                for child in tree[node]:
                    temp = dfs(child)
                    if s[parent[child]] == -1 or s[child] != s[parent[child]]:
                        if temp > max1:
                            max2 = max1
                            max1 = temp
                        elif temp > max2:
                            max2 = temp
                result = max(result, 1 + max1 + max2)
                return 1 + max(max1, max2)
            dfs(root)
            return result
