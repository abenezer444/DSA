class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for char in ascii_lowercase:
            arr=[]
            for word in words:
                arr.append(word.count(char))
            for _ in range(min(arr)):
                ans.append(char)
        return ans
            
            
            
            
            
        
                
                
                
        