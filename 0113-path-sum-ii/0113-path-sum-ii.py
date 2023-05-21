# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def backtrack(node,curPath,curSum):
            
            if not node:
                return
            curPath.append(node.val)
            if (not node.left) and (not node.right) and (not curSum-node.val):
              
                ans.append(curPath[:])
                
            
            backtrack(node.left,curPath,curSum - node.val)
            backtrack(node.right,curPath,curSum - node.val)
            curPath.pop()
        backtrack(root,[],targetSum)
        return ans
                
                
                
        