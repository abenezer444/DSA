class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_map = defaultdict(int)
        pairs = 0
        for num in arr:
    
            
            cur_mod = num % k
            compliment = (k - cur_mod) % k
            
            if compliment in remainder_map:
                pairs += 1
                remainder_map[compliment] -= 1
                
                if not remainder_map[compliment]:
                    del remainder_map[compliment]
            else:
                remainder_map[cur_mod] += 1
       
        
        return pairs == len(arr)//2
                
            
        
        