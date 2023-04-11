# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            
            string = str(node.val)

            if node.left:
                string += '('+dfs(node.left)+')'
            if not node.left and node.right:
                string += '()'
            if node.right:
                string += '('+dfs(node.right)+')'
                
            return string
                
        
        return dfs(root)
                
        