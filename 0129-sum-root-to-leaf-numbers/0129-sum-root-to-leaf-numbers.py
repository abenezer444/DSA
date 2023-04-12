# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def numGenerator(arr):
            num = 0
            for i in range(len(arr)):
                num += arr[i]*(10**(len(arr)-i-1))
            return num
        
                
                
        def dfs(node,path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                self.ans += numGenerator(path[:])
                path.pop()
                return
            
            dfs(node.left,path)
            dfs(node.right,path)
            path.pop()
        dfs(root,[])

        return self.ans
            
        