class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowHash, colHash, total = {}, {}, 0
        for i in range(len(grid)):
            row = ()
            for j in range(len(grid)):
                row += (grid[i][j],)
            rowHash[row] = rowHash.get(row, 0) + 1
        
        for i in range(len(grid)):
            col = ()
            for j in range(len(grid)):
                col += (grid[j][i],)
            colHash[col] = colHash.get(col, 0) + 1
        
        for key in colHash:
            if key in rowHash:
                total += colHash[key] * rowHash[key]
        
        return total
        

        