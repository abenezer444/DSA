class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        reversedGrid=[[0 for i in range(rows)] for h in range(columns)]
       
        count=0
        for row in range(rows):
            for column in range(columns):
                reversedGrid[column][row]=grid[row][column]
        print(grid)
        print(reversedGrid)
        for gri in grid:
            if gri in reversedGrid:
                count+=reversedGrid.count(gri)
        return count
        
        
        