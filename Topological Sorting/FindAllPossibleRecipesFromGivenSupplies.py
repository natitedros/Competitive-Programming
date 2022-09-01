class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        supplies = set(supplies)
        for i in range(len(ingredients)):
            ingredients[i] = set(ingredients[i])
        inDegree = [0]*n
        q = deque()
        res = []
        for i in range(n):
            for ing in ingredients[i]:
                if ing not in supplies:
                    inDegree[i] += 1
            if inDegree[i] == 0:
                q.append(i)
                res.append(recipes[i])        
        while q:
            ind = q.popleft()
            for i in range(n):
                if inDegree[i]:
                    if recipes[ind] in ingredients[i]:
                        inDegree[i] -= 1
                    if not inDegree[i]:
                        q.append(i)
                        res.append(recipes[i])
        return res
                