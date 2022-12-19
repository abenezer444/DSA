class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        width=len(matrix[0])
        rows=set()
        columns=set()
        for i in range(length):
            for j in range(width):
                if matrix[i][j]==0:
                    rows.add(i)
                    columns.add(j)
        for row in rows:
            for j in range(width):
                matrix[row][j]=0
        for column in columns:
            for j in range(length):
                matrix[j][column]=0
        
        
        