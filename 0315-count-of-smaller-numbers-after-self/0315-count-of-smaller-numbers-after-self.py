class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        nums = [(num,idx) for idx,num in enumerate(nums)]
      
        
        def merge(left, right):
            result = []
            l = 0
            r = 0


            while l<len(left) and r<len(right):

                if left[l][0] < right[r][0]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                
            while l<len(left):
                result.append(left[l])
                l+=1
            while r<len(right):
                result.append(right[r])
                r+=1
        
            return result
        def mergeSort(left, right, arr):
    
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            
           
            r = 0
            for l in range(len(left_half)):
               
                while r<len(right_half) and left_half[l][0] > right_half[r][0]:
                    r+=1
                answer[left_half[l][1]] += r
                
            

            return merge(left_half, right_half)
        mergeSort(0,len(nums)-1,nums)
        return answer
        