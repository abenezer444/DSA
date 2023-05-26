class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(low,mid,high):
            cnt=0
            j=mid+1
            for i in range(low,mid+1):
                while j<=high and nums[i]>2*(nums[j]):
                    j+=1
                cnt+=j-(mid+1)
            temp=[]
            left=low
            right=mid+1
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1    
                    
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
                
            for i in range(low,high+1):
                nums[i]=temp[i-low]
            return cnt
        def mergeSort(low,high):
            if low>=high:
                return 0
            mid=(low+high)//2
            inv=mergeSort(low,mid)
            inv+=mergeSort(mid+1,high)
            inv+=merge(low,mid,high)
            return inv
        
        return mergeSort(0,len(nums)-1)