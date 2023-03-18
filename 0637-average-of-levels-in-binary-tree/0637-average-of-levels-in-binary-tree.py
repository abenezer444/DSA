# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque([root])
        ans = []
        
        while queue:
            length = len(queue)
            summ = 0
            for i in range(length):
                popped = queue.popleft()
                summ += popped.val
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            
            ans.append((float(summ)/length))
        return ans
                
        