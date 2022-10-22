# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.ans=0
        def inorder(node,ans=0):
            if node:
                inorder(node.left)
                if low<=node.val<=high:
                    self.ans+=node.val
                inorder(node.right)
        inorder(root)
        return self.ans
        