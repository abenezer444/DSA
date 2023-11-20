class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        
        for word in words:
            for char in word:
                indegree[char] = 0
        
        
        for i in range(1, len(words)):
            word_one = words[i-1]
            word_two = words[i]
            
            
            for j in range(len(min(word_one, word_two))):
                char_one = word_one[j]
                char_two = word_two[j]
                
                
                if char_one != char_two:
                    if (char_two not in graph[char_one]):
                        graph[char_one].add(char_two)
                    
                        indegree[char_two] += 1
                    break
            else:
                if len(word_one) > len(word_two):
                    return ''
        
        queue = deque()
        
        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)
        top_sort = []
        while queue:
            cur = queue.popleft()
            top_sort.append(cur)
            
            for child in graph[cur]:
                indegree[child] -= 1
                if not indegree[child]:
                    queue.append(child)
       
                    
        return ''.join(top_sort) if len(top_sort) == len(indegree) else ''
            
        