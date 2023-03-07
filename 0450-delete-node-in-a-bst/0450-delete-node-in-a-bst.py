# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getInorderSuccesor(node):
            node = node.right
            while node.left:
                node = node.left
            return node
                
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if (not root.right) and (not root.left):
                return None
            elif (not root.left) and root.right:
                root = root.right
        
                return root
            elif (not root.right) and root.left:
                root = root.left
                
                return root
            else:
                temp = getInorderSuccesor(root)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)

                
                return root
            
                
            
        return root
            
        