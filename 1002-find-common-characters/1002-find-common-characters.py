class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for char in ascii_lowercase:
            arr=float('inf')
            for word in words:
                count=word.count(char)
                if count<arr:
                    arr=count
            for _ in range(arr):
                ans.append(char)
        return ans
            
            
            
            
            
        
                
                
                
        