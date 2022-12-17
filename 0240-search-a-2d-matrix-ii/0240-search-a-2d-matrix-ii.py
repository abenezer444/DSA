class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #start from the top corner
        #if topcorner>target go left
        #else go down
        rows=len(matrix)
        columns=len(matrix[0])-1
        row=0
        column=columns
        while row<rows and column>=0:
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                row+=1
            else:
                column-=1
        return False
        
        