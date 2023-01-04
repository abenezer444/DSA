class Solution:
    def countPairs(self, sweetness: List[int]) -> int:
        powers=[2**i for i in range(22)]
     
        count=0
        
        for power in powers:
            diffMap=defaultdict(int)
            
            for sweet in sweetness:
                
                diff=power-sweet
                
                if diff in diffMap:
                    
                    count+=diffMap[diff]
                    diffMap[sweet]+=1
                    
                else:
                    diffMap[sweet]+=1
        return count%(10**9+7)
                    
                
            
            
       
        
            
        
        