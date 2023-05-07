class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapify(piles)
        for i in range(k):
            removed = -heappop(piles)
            removed -= floor(removed/2)
            heappush(piles,-removed)
        return -sum(piles)
        