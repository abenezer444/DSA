class Solution:
    def firstUniqChar(self, s: str) -> int:
        countMap = Counter(s)
        
        ans = -1
        
        for i in range(len(s) - 1, -1, -1):
            
            char = s[i]
            
            if countMap[char] == 1:
                ans = i
        
        return ans 