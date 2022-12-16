class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        check=''
        for i in s:
            if i.isalnum():
                check+=i
        if check==check[::-1]:
            return True
        return False