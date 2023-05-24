class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = []
        def trav(root):
            if not root:
                return None
            temp = dfs(root,[])
            if root.val == sum(temp)//len(temp):
                self.res.append(root.val)

            if root.left:
                trav(root.left)
            
            if root.right:
                trav(root.right)


        def dfs(root,final):
            if not root:
                return None
            
            final.append(root.val)

            if root.left:
                dfs(root.left,final)
            
            if root.right:
                dfs(root.right,final)
            
            return final
        
        trav(root)
        return len(self.res)