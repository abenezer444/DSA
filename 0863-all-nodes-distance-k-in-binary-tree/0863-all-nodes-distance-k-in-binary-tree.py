# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.k = k
        graph = defaultdict(list)
        
        def bfs(node):
            queue = deque([node])
            
            while queue:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    graph[cur.val].append(cur.left.val)
                    graph[cur.left.val].append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                    graph[cur.val].append(cur.right.val)
                    graph[cur.right.val].append(cur.val)
        bfs(root)
        visited = set()
        def gbfs(node):
            ans = []
            queue = deque([(node,0)])
            visited.add(node)
            while queue:
                cur,depth  = queue.popleft()
                if depth == self.k:
                    ans.append(cur)
                for child in graph[cur]:
                    if child not in visited:
                        visited.add(child)
                        queue.append((child,depth + 1))
            return ans
        return gbfs(target.val)
            
            