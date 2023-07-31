class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(row,col):
            if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                return True
            return False
        directions = [(1,0),(1,1),(1,-1)]

        for i in range(len(matrix) - 2,-1,-1):
            for j in range(len(matrix[0]) - 1,-1,-1):
                minn = float('inf')
                for direction in directions:
                    new_row = i + direction[0]
                    new_col = j + direction[1]
                    if inbound(new_row,new_col):
                        minn = min(minn,matrix[new_row][new_col])
                        
                matrix[i][j] += minn
        print(matrix)
        return min(matrix[0])

                
                
        