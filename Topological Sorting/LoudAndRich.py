class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        superior = defaultdict(list)
        
        for rich, poor in richer:
            superior[poor].append(rich)
            
        cache = {}
        def dfs(person):
            if person in cache:
                return cache[person]
            cache[person] = person
            for rich_person in superior[person]:
                temp = dfs(rich_person)
                if quiet[temp] < quiet[cache[person]]:
                    cache[person] = temp
            return cache[person]
        
        res = []
        for person in range(len(quiet)):
            res.append(dfs(person))
        return res
#Edited
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        superior = defaultdict(list)
        
        for rich, poor in richer:
            superior[poor].append(rich)
        cache = {}
        res = []
        for person in range(len(quiet)):
            res.append(self.dfs(person,cache,quiet,superior))
        return res
    
    def dfs(self,person,cache,quiet,superior):
        if person in cache:
            return cache[person]
        cache[person] = person
        for rich_person in superior[person]:
            temp = self.dfs(rich_person,cache,quiet,superior)
            if quiet[temp] < quiet[cache[person]]:
                cache[person] = temp
        return cache[person]
        
        