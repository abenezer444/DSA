# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodeMap = defaultdict(list)
        def traverse(node,depth):
            if node:
                nodeMap[depth].append(node.val)
                traverse(node.left,depth+1)
                traverse(node.right,depth+1)
            return node
        traverse(root,0)
        ans = []
        for value in nodeMap.values():
            ans.append(value[-1])
            
   
  
        return ans
        