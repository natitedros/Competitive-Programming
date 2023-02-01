class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:        
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] + mat[r - 1][c - 1] - prefix[r - 1][c - 1]

        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                res[r][c] = prefix[min(r + k + 1, rows)][min(c + k + 1, cols)] - \
                    prefix[max(r - k, 0)][min(c + k + 1, cols)] - \
                    prefix[min(r + k + 1, rows)][max(c - k, 0)] + \
                    prefix[max(r - k, 0)][max(c - k, 0)]
        
        return res