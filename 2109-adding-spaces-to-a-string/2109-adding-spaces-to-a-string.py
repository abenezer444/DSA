class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces=set(spaces)
        ans=''
        for i in range(len(s)):
            if i in spaces:
                ans+=' '
            ans+=s[i]
        return ans
        