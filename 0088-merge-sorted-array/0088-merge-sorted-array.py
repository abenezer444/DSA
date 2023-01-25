class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        zero=m+n-1
        left=m-1
        right=n-1
        
        while right>=0 :
            if left<0 or nums1[left]<=nums2[right]:
                nums1[zero]=nums2[right]
                zero-=1
                right-=1
            else:
                nums1[left],nums1[zero]=nums1[zero], nums1[left]
                zero-=1
                left-=1
            
                
        