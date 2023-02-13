class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        spiral = []
        while left<right and top<bottom:
            #going right
            for i in range(left,right):
                spiral.append(matrix[top][i])
            top+=1
            #going down
            for i in range(top,bottom):
                spiral.append(matrix[i][right-1])
            right-=1
            if left>=right or top>=bottom:
                break
            #going left
            for i in range(right-1,left-1,-1):
                spiral.append(matrix[bottom-1][i])
            bottom-=1
            # print(matrix[bottom][left])
            
            #going up
            for i in range(bottom-1,top-1,-1):
                spiral.append(matrix[i][left])
            left+=1
        return spiral
          
                
            
        