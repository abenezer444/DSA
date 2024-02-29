# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        tuple_list = []
        def recur(col, row, node):
            if not node:
                return
            tuple_list.append([col, row, node.val])
            
            recur(col - 1, row + 1, node.left)
            recur(col + 1, row + 1, node.right)
        recur(0,0,root)
        
        tuple_list.sort()
        
        vertical_order = []
        
        
        cur_col = tuple_list[0][0]
        current_vertical_order = []
       
        for col, row, val in tuple_list:
            
            
            if cur_col == col:
                current_vertical_order.append(val)
                
            else:
                vertical_order.append(current_vertical_order)
                current_vertical_order = [val]
                cur_col = col
        
        vertical_order.append(current_vertical_order)
    
            
        
        return vertical_order
        