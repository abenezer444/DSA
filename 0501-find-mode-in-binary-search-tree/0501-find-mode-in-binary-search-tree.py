# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        sortedArr = []
        ans = []
        def inorder(node):
            if node:
                inorder(node.left)
                sortedArr.append(node.val)
                inorder(node.right)
        inorder(root)
        counter = Counter(sortedArr)
        maxx = max(counter.values())
        for key in counter:
            if counter[key] == maxx:
                ans.append(key)
        return ans
            
                