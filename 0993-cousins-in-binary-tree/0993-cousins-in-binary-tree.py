# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        
        queue = deque([root])
        
        while queue:
            length = len(queue)
            checker = {}
            for i in range(length):
                popped = queue.popleft()
                
                if popped.left:
                    queue.append(popped.left)
                    checker[popped.left.val] = popped.val
                if popped.right:
                    queue.append(popped.right)
                    checker[popped.right.val] = popped.val
            
            if x in checker and y in checker and checker[x]!=checker[y]:
                return True
        return False
                

        