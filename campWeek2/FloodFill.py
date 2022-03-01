class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        stk = []
        visited = set()
        m = len(image)
        n = len(image[0])
        stk.append([sr,sc])
        while stk:
            v = stk.pop()
            sr = v[0]
            sc = v[1]
            image[sr][sc] = newColor
            visited.add((sr,sc))
            if sr-1>=0 and image[sr-1][sc] == oldColor and not (sr-1,sc) in visited:
                stk.append([sr-1,sc])
            if sc-1>=0 and image[sr][sc-1] == oldColor and not (sr,sc-1) in visited:
                stk.append([sr,sc-1])
            if sr+1<m and image[sr+1][sc] == oldColor and not (sr+1,sc) in visited:
                stk.append([sr+1,sc])
            if sc+1<n and image[sr][sc+1] == oldColor and not (sr,sc+1) in visited:
                stk.append([sr,sc+1])
        return image