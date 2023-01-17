class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonalMap=defaultdict(list)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                diagonalMap[row-col].append(matrix[row][col])
        temp=[]
        for value in diagonalMap.values():
            temp.append(len(set(value))==1)
        if all(temp) and temp[0]==True:
            return True
        else:
            return False
            
        