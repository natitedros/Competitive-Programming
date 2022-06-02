class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        res = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])
            res.append(temp)
        return res