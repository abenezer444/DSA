class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        maxx = max(nums)+1
        sieve = [set() for i in range(maxx)]
        # count = 2
        
        for i in range(2,maxx):
            if sieve[i]:
                continue
            
            j = 1
            while i*j < maxx:
                sieve[i*j].add(i)
                j+=1
        
            
            
        new_nums= [sieve[num] for num in nums]
        
        return len(reduce(lambda a , b : a.union(b) , new_nums))              
        