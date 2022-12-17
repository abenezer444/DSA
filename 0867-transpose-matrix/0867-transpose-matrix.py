class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        columns=len(matrix[0])
        result=[[0]*rows for x in range(columns)]
        for row in range(rows):
            for column in range(columns):
                result[column][row]=matrix[row][column]
        return result
        