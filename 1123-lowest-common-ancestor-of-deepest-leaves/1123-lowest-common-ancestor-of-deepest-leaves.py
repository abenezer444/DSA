# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest = set()
        nodeDepth = {}
        maxx = float('-inf')
        def dfs(node,depth):
            nonlocal maxx
            if node:
                maxx = max(maxx,depth)
                nodeDepth[node.val] = depth
                dfs(node.left,depth + 1)
                dfs(node.right,depth + 1)
        dfs(root,0)
        for node in nodeDepth:
            if nodeDepth[node] == maxx:
                deepest.add(node)
        def postorder(node):
            if not node or node.val in deepest:
                return node
            left = postorder(node.left)
            right = postorder(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        return postorder(root)