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
        arr = []
        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root)
        
        dummy = TreeNode()
        temp = dummy
        for num in arr:
            dummy.right = TreeNode(num)
            dummy = dummy.right
        return temp.right
               
                

                
        