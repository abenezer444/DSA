# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #iterative solution
        stop=0
        stack=[]
        cur=root
        while cur or stack:
            #go left as far as possible and add the nodes to the stack
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            stop+=1
            if k==stop:
                return cur.val
            #check the right
            cur=cur.right
            