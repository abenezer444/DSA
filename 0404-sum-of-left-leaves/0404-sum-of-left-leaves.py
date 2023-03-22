# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def traverse(node):
            if node:
                if node.left and not node.left.left and not node.left.right:
                    self.sum += node.left.val
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return self.sum
        