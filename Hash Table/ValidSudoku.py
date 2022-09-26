class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid(row):
            nums = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in nums:
                    return False
                nums.add(board[row][j])
            return True
        def isColValid(col):
            nums = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in nums:
                    return False
                nums.add(board[i][col])
            return True
        def isBoxValid(row1,row2,col1,col2):
            nums = set()
            for i in range(row1,row2+1):
                for j in range(col1,col2+1):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])
            return True
        for i in range(9):
            if not (isRowValid(i) and isColValid(i)):
                return False
        box = [[0,2],[3,5],[6,8]]
        for r in box:
            for c in box:
                if not isBoxValid(r[0],r[1],c[0],c[1]):
                    return False
        return True