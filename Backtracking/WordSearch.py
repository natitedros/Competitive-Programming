class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        freq = defaultdict(int)
        for i in range(len(board)):
            for j in range(len(board[0])):
                freq[board[i][j]] += 1
        charCount = Counter(word)
        for key in charCount.keys():
            if charCount[key] > freq[key]:
                return False
        def isInside(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(index, row, col, visited):
            if index == len(word):
                return True
            for r, c in directions:
                newR, newC = row+r, col+c
                if isInside(newR, newC) and (newR, newC) not in visited and board[newR][newC] == word[index]:
                    visited.add((newR, newC))
                    if dfs(index+1, newR, newC, visited):
                        return True
                    visited.remove((newR, newC))
            return False
                    
        visited = set()                   
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j, visited):
                        return True
                    visited.remove((i, j))
        return False