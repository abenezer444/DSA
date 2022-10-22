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
        def inorder(node1,node2):
            if node1 and node2:
                #go left
                inorder(node1.left,node2.left)
                #perform action
                if node1 is target:
                    self.ans=node2
                #go right
                inorder(node1.right,node2.right)
        inorder(original,cloned)
        return self.ans
    
        
            
                
       
                
            
        