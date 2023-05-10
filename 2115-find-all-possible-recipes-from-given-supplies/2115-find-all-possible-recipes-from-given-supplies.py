class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        ans = []
        queue = deque()
        
        for supply in supplies:
            queue.append(supply)
            
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for i in range(len(ingredients)):
            ingredient = ingredients[i]
            for ing in ingredient:
                indegree[recipes[i]] += 1
                graph[ing].append(recipes[i])
    
        while queue:
            node = queue.popleft()
            for child in graph[node]:
               
                indegree[child] -= 1
                if indegree[child] == 0:
                    ans.append(child)
                    queue.append(child)
          
        return ans  
        
            
        