class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        check=''
        for i in s:
            if i.isalnum():
                check+=i
        left=0
        right=len(check)-1
        while left<right:
            if check[left]!=check[right]:
                 return False
            left+=1
            right-=1
            
                
        return True
       