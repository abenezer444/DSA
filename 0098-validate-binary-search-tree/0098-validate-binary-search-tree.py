# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node,arr):
            if node:
                inorder(node.left,arr)
                arr.append(node.val)
                inorder(node.right,arr)
        arr = []
        inorder(root,arr)
        ans = True
        for i in range(1,len(arr)):
            if arr[i-1] >= arr[i]:
                ans = False
        return ans
            
       