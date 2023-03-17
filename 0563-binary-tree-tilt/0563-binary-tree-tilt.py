# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def traverse(node):
            if not node:
                return 0
            left =  traverse(node.left)
            right = traverse(node.right)
            ans[0] += abs(left-right)
            return node.val + left + right
        traverse(root)
        return ans[0]
            
                
            
        