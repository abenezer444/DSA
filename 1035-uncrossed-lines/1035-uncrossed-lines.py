class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def recur(i,j):
            ans = 0
            if i == len(nums1) or j == len(nums2):
                return 0
            if nums1[i] == nums2[j]:
                ans += 1 + recur(i + 1, j + 1)
                
            else:
                ans += max(recur(i + 1, j),recur(i, j + 1))
                
            return ans
        return recur(0, 0)