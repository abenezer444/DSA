# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans=[]
        def inorder(node):
            if node:
                inorder(node.left)
                self.ans.append(node.val)
                inorder(node.right)
        inorder(root)
        return self.ans[k-1]