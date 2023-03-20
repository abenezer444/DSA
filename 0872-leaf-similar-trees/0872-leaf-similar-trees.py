# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafNodes1 = []
        leafNodes2 = []
        def traverse1(node,arr):
            if node:
                if not node.left and not node.right:
                    arr.append(node.val)
                traverse1(node.left,arr)
                traverse1(node.right,arr)
        
        traverse1(root1,leafNodes1)
        traverse1(root2,leafNodes2)
        
        return leafNodes2 == leafNodes1
        
                    
        