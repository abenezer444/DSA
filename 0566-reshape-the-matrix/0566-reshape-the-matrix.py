class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        length=len(mat)
        width=len(mat[0])
        if r*c==length*width:
            elements=[]
            for row in range(length):
                for col in range(width):
                    elements.append(mat[row][col])
            reshape=[[0 for col in range(c)] for row in range(r)]
            index=0
            for row in range(r):
                for col in range(c):
                    reshape[row][col]=elements[index]
                    index+=1
            return reshape
        return mat
                
        
        