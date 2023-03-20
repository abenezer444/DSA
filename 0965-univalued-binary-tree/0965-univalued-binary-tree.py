# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.target = root.val
        self.ans = True
        def traverse(node):
            if node:
                if node.val != self.target:
                    self.ans = False
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return self.ans
                
        