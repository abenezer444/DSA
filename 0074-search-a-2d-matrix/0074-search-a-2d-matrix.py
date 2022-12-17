class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #determine the row
        #search in the row
        result=False
        
        #helper function to search through the row
        def searchRow(row):
            l=0
            r=len(row)-1
            while l<=r:
                mid=(l+r)//2
                if row[mid]==target:
                    return True
                elif row[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        #find the row
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][-1]<target:
                left=mid+1
            elif matrix[mid][-1]>target:
                result=searchRow(matrix[mid])
                right=mid-1
            else: return True
        return result
        
            
            