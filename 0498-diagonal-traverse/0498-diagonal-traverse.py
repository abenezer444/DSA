class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        asDiagonal=[]
        rows=len(mat)
        cols=len(mat[0])
        diagonals=[[] for _ in range(rows+cols-1)]
        
        for row in range(rows):
            for col in range(cols):
                diagonals[col+row].append(mat[row][col])
        
        for index in range(len(diagonals)):
            if index%2==0:
                asDiagonal.extend(diagonals[index][::-1])
            else:
                asDiagonal.extend(diagonals[index])
        
        return asDiagonal
        