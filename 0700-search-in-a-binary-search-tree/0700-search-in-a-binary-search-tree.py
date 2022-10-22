# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.ans=None
        def preorder(node):
            if node:
                if node.val==val:
                    self.ans=node
                    return
                if node.val>val:
                    preorder(node.left)
                else:
                    preorder(node.right)
        preorder(root)
        return self.ans
            
        