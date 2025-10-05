class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q=[]
        for num in nums:
            heapq.heappush(q, -num)

        res=0
        while k:
            k-=1
            res = -heapq.heappop(q)
        return res