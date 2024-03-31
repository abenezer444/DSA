class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_map = defaultdict(int)
        pairs = 0
        for num in arr:
    
            
            cur_mod = num % k
            
            if (k - cur_mod) % k in remainder_map:
                pairs += 1
                remainder_map[(k - cur_mod) % k] -= 1
                
                if not remainder_map[(k - cur_mod) % k]:
                    del remainder_map[(k - cur_mod) % k]
            else:
                remainder_map[cur_mod] += 1
       
        
        return pairs == len(arr)//2
                
            
        
        