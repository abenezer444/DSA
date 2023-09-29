from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        
        def backtrack(start, path):
            if start == len(s):
                ans.append(' '.join(path))
                return
            
            for word in wordDict:
                if s.startswith(word, start):
                    path.append(word)
                    backtrack(start + len(word), path)
                    path.pop()
        
        backtrack(0, [])
        return ans
