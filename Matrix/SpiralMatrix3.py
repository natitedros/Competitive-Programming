class Solution:
    def isInbound(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        #go two directions with the same length
        #start from the given index
        #if the indices are inbound, append the (row,col)
        dx, dy = 0, 1 
        answer = []
        steps = 1
        answer.append((rStart, cStart))
        length = 1
        
        while length < rows*cols:
            for i in range(steps):
                rStart += dx
                cStart += dy
                if self.isInbound(rStart, cStart, rows, cols):
                    length += 1
                    answer.append((rStart,cStart))
            
            if dx == 1 or dx == -1:
                steps += 1
                
            #spirals by changing the direction
            dx, dy = dy, -dx
            
        return answer
