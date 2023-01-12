class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        indexCharMap=defaultdict(list)
        for i in range(len(strs[0])):
            for word  in strs:
                indexCharMap[i].append(word[i])
        count=0
        for value in indexCharMap.values():
            for index in range(1,len(value)):
                if value[index]<value[index-1]:
                    count+=1
                    break
        return count
                
        