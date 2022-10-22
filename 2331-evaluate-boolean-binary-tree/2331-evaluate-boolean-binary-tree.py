# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if node:
                if not node.left and not node.right:
                    if node.val==0:
                        return False
                    else:
                        return True
                elif node.val==2:
                    return check(node.right) or check(node.left)
                else:
                    return check(node.right) and check(node.left)
            else: return True
        return check(root)
                
        