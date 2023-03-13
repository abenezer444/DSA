# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        myQueue = deque()
        myQueue.append([root])
        
        while myQueue:
            n = len(myQueue)
            for i in range(n):
                node = myQueue.popleft()[0]
              
                if node.left:
                    myQueue.append([node.left])
                if node.right:
                    myQueue.append([node.right])
                if i == n-1:
                    ans.append(node.val)
                    
        
        
        return ans