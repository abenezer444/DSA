# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        
        def inorder(node):
            if not node:
                return 
            
            if node:
                if node.val == target.val:
                   
                    return node
                left = inorder(node.left)
                right = inorder(node.right)
                
                if left:
                    return left
                return right
     
        
        return inorder(cloned)
    
        
            
                
       
                
            
        