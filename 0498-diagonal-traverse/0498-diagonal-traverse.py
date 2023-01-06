class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        asDiagonal=[]
        rows=len(mat)
        cols=len(mat[0])
        diagonals=[[] for _ in range(rows+cols-1)] #the number of diagonals has this mathematical relationship 
        
        for row in range(rows):
            for col in range(cols):
                diagonals[col+row].append(mat[row][col]) #summing the col and the row gives the index of the diagonal on which htis element will end up
        
        for index in range(len(diagonals)):
            if index%2==0:
                asDiagonal.extend(diagonals[index][::-1])
            else:
                asDiagonal.extend(diagonals[index])
        
        return asDiagonal
        