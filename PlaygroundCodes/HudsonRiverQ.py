def solve(table):
    row = len(table)
    col = len(table[0])
    result = [[0 for _ in range(col)] for _ in range(row)]
    for r in range(row):
        new_col = r//2
        startRow = 0
        if not r%2:
            startRow = 1
        for i in range(startRow, row, 2):
            result[i][new_col] = table[r][i//2]
    return result
    print(result)   
solve([["a", "b"],["c","d"],["e", "f"],["g", "h"]])
