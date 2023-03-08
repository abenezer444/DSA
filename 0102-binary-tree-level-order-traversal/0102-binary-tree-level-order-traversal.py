# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeMap = defaultdict(list)
        def traverse(node,depth):
            if node:
                nodeMap[depth].append(node.val)
                traverse(node.left,depth+1)
                traverse(node.right,depth+1)
            return node
        depth = 0
        traverse(root,depth)
   
  
        return nodeMap.values()
        