class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        k=k%len(nums)
#         while l<r:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#             r-=1
    
#         l,r=0,k-1
#         while l<r:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#             r-=1
#         l,r=k,len(nums)-1
#         while l<r:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
#             r-=1
        def helper(self,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        helper(self,0,len(nums)-1)
        helper(self,0,k-1)
        helper(self,k,len(nums)-1)
                
        
        
        
        