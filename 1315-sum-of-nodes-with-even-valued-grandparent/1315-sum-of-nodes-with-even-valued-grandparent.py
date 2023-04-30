# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        parent = TreeNode(-1)
        grandParent = TreeNode(-1)
        
        def dfs(node,parent,grandParent):
            if node:
                if grandParent.val % 2 == 0:
                    self.total += node.val

                dfs(node.left,node,parent)
                dfs(node.right,node,parent)
        
        dfs(root,parent,grandParent)
        
        return self.total
        
            