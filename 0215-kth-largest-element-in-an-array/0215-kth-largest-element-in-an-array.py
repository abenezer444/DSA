class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        def partition(arr, left, right, pivot):
            arr[pivot], arr[right] = arr[right], arr[pivot]
            pivot_value = arr[right]
            store_index = left
            for i in range(left, right):
                if arr[i] < pivot_value:
                    arr[i], arr[store_index] = arr[store_index], arr[i]
                    store_index += 1
            arr[store_index], arr[right] = arr[right], arr[store_index]
            return store_index

        def quickSort(arr, left, right, k):
            if left == right:
                return arr[left]
            pivot = (left + right) // 2
            pivot = partition(arr, left, right, pivot)
            if k == len(arr) - pivot:
                return arr[pivot]
            elif k < len(arr) - pivot:
                return quickSort(arr, pivot + 1, right, k)
            else:
                return quickSort(arr, left, pivot - 1, k)

        return quickSort(arr, 0, len(arr) - 1, k)
