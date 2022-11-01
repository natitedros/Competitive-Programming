class Solution:
    def find(self, node, parent):
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
        return parent[node]
    
    def hasCycle(self, node1, node2, parent, rank):
        parent1 = self.find(node1, parent)
        parent2 = self.find(node2, parent)
        
        if parent1 == parent2:
            return True
        
        if rank[parent1] > rank[parent2]:
            parent[parent2] = parent1
        elif rank[parent2] > rank[parent1]:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1
            rank[parent1] += 1
        
        return False
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0]*(len(edges)+1)
        rank = [1]*(len(edges)+1)
        for i in range(len(edges)+1):
            parent[i] = i
        for node1, node2 in edges:
            if self.hasCycle(node1, node2, parent, rank):
                return [node1, node2]
        
        