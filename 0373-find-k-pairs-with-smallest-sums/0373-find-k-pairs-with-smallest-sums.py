class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set((0,0))
        ans = []
        minHeap = [(nums1[0]+nums2[0],(0,0))]
        while minHeap and k:
           
            summ,pair = heappop(minHeap)
            
            
            ans.append((nums1[pair[0]],nums2[pair[1]]))
            k -= 1 
            i,j = pair
            if i+1 < len(nums1):
                if (i+1,j) not in visited:
                    heappush(minHeap,(nums1[i+1]+nums2[j],(i+1,j)))
                    visited.add((i+1,j))
            if j+1 < len(nums2):
                if (i,j+1) not in visited:
                    heappush(minHeap,(nums1[i]+nums2[j+1],(i,j+1)))
                    visited.add((i,j+1))
                
        return ans
            
        