class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        l=0
        ranges=[]
        visited={}
        while l<len(s):
            start=l
            r=0
            while r<len(s):
                if s[r]==s[l] and s[r] not in visited:
                    end=r
                    ranges.append([start,end])
                r+=1
            visited[s[l]]=1
            l+=1
        stack=[[ranges[0][0],ranges[0][1]]]
        for i in ranges[1:]:
            if stack:
                if (stack[-1][1]>=i[0] or stack[-1][1]>=i[1]) and stack[-1][0]<=i[0]:
                    stack[-1][1]=max(i[0],i[1],stack[-1][1])
                else:stack.append([i[0],i[1]])
        res=[]
        for i in stack:
            res.append(i[1]-i[0]+1)
        return res

        


