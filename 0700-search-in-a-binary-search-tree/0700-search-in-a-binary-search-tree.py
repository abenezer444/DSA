# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None
        
        
        def search(node):
            if not node:
                return None
            if node.val == val:
                self.ans = node
                return
            elif node.val > val:
                search(node.left)
            else:
                search(node.right)
        search(root)
        return self.ans