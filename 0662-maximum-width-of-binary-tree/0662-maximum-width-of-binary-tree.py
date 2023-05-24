# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        deq = collections.deque([(root, 1)])
        max_w = 0
        
        while deq:
		    
            if deq[0][1] != deq[-1][1]:
                max_w = max(max_w, (1 + deq[-1][1] - deq[0][1]))
            for i in range(len(deq)):
                node, cur = deq.popleft() 
                if node.left: 
                    deq.append((node.left, cur * 2 - 1))   
                if node.right: 
                    deq.append((node.right, cur * 2))  
                    
        return max(1, max_w)
        