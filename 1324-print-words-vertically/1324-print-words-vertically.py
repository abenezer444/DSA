class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        longest=len(s[0])
        for index in range(1,len(s)):
            if len(s[index])>longest:
                longest=len(s[index])
        indexCharMap=defaultdict(list)
        for index in range(longest):
            for word in s:
                if index<len(word):
                    indexCharMap[index].append(word[index])
                else:
                    indexCharMap[index].append(' ')
        result=[]
        print(indexCharMap)
        for word in indexCharMap.values():
            result.append("".join(word).rstrip())
        return result
        
        