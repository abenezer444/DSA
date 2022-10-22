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
        self.fake=TreeNode(0)
        self.fake1=self.fake
        
        def inorder(node):
            if node: 
                inorder(node.left)
                node.left=None
                self.fake.right=node
                self.fake=node
                inorder(node.right)
        inorder(root)
        return self.fake1.right
               
                

                
        