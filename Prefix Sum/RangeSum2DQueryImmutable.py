class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.d = defaultdict(int)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                self.d[(i,j)] = matrix[i][j] + self.d[(i+1,j)] + self.d[(i,j+1)] - self.d[(i+1,j+1)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.d[(row1,col1)] - self.d[(row1,col2+1)] - self.d[(row2+1,col1)] + self.d[(row2+1,col2+1)]