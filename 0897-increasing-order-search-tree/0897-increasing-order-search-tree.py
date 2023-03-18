# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode()
        ans = TreeNode(right=dummy)
        stack = []
   
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            popped = stack.pop()
            dummy.right = popped
            dummy = dummy.right
            dummy.left = None
            
            current = popped.right
        
            
        return ans.right.right
               
                

                
        