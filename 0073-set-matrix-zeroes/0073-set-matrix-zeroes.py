class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        width=len(matrix[0])
        zeros=[]
        for row in range(length):
            for col in range(width):
                if matrix[row][col]==0:
                    zeros.append([row,col])
        for zero in zeros:
            rows=zero[0]
            cols=zero[1]
            for row in range(length):
                matrix[row][cols]=0
            for col in range(width):
                matrix[rows][col]=0
        