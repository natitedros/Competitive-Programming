class Solution:
    def boxNumber(self, i, j):
        return ((i//3) * 3) + (j//3)
    def nextRowCol(self, row, col):
        nextRow = row + (col+1)//9
        nextCol = (col+1) % 9
        return (nextRow, nextCol)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[self.boxNumber(i, j)].add(board[i][j])
    
        def fillBox(i, j):
            if i == 9:
                return True
            num = self.boxNumber(i, j)
            nr, nc = self.nextRowCol(i, j)
            if board[i][j] != ".":
                return fillBox(nr, nc)
            else:
                for val in range(1, 10):
                    if str(val) not in row[i] and str(val) not in col[j] and str(val) not in box[num]:
                        row[i].add(str(val))
                        col[j].add(str(val))
                        box[num].add(str(val))
                        board[i][j] = str(val)
                        if fillBox(nr, nc):
                            return True
                        row[i].remove(str(val))
                        col[j].remove(str(val))
                        box[num].remove(str(val))
                        board[i][j] = "."
                return False
        fillBox(0, 0)      