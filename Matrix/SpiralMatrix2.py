# Iterative Method
class Solution:
    def isInside(self,row,col,n):
        return 0 <= row < n and 0 <= col < n
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        length = n**2
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        pointer = 0
        num = 1
        row, col = 0, 0
        
        while num <= length:
            matrix[row][col] = num
            visited.add((row,col))
            num += 1
            dr, dc = directions[pointer]
            
            if (row+dr, col+dc) in visited or not self.isInside(row+dr, col+dc, n):
                pointer = (pointer+1) % 4
                dr, dc = directions[pointer]
            
            row += dr
            col += dc
        
        return matrix
# Recursive Method  
class Solution:
    def isInside(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
    
    def buildSpiralMatrix(self, directions, matrix, visited, pointer, num, row, col):
        if num > (len(matrix))**2:
            return
        
        matrix[row][col] = num
        visited.add((row,col))
        dr, dc = directions[pointer]
        
        if not self.isInside(row+dr, col+dc, len(matrix)) or (row+dr, col+dc) in visited:
            pointer = (pointer+1) % 4
            dr, dc = directions[pointer]
        
        self.buildSpiralMatrix(directions, matrix, visited, pointer, num+1, row+dr, col+dc)
        
    
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        length = n**2
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        self.buildSpiralMatrix(directions, matrix, visited, 0, 1, 0, 0)
        
        return matrix
        
                   