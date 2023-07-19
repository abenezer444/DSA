# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def recur(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            left =  node.val + (recur(node.left.left)+recur(node.left.right)) if node.left else node.val
            right = node.val + (recur(node.right.left)+recur(node.right.right)) if node.right else node.val
            pick = left+right-node.val
            notPick = recur(node.left) + recur(node.right)
            return max(pick,notPick)
        return recur(root)
        