class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0
        right=0
        ans=[]
        while right<len(chars):
            while right<len(chars) and chars[left]==chars[right]:
                right+=1
            ans.append(chars[left])
            if right-left!=1:
                times=str(right-left)
                ans.extend(list(times))
            left=right
        for i in range(len(ans)):
            chars[i]=ans[i]
        return len(ans)
            
        