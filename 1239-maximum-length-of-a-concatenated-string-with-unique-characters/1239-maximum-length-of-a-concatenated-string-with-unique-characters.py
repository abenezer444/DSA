class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max = 0
        
        def isUnique(string1,string2):
            return (not set(string1).intersection(set(string2))) and len(string1)==len(set(string1)) and len(string2)==len(set(string2))
        
        def backtrack(cur,index):
           
            self.max = max(self.max,len(''.join(cur)))
            if index>=len(arr):
                return 
            if isUnique(''.join(cur),arr[index]):
                cur.append(arr[index])
                backtrack(cur,index+1)
                cur.pop()
            backtrack(cur,index+1)
        backtrack([],0)
        return self.max
        