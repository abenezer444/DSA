# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def backTrack(node, path):
            
            if not node:
                return 
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(path))
        
            backTrack(node.left, path)
            backTrack(node.right, path)
            path.pop()
        backTrack(root,[])
        return paths
                
        