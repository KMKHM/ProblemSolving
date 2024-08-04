"""
1508. Range Sum of Sorted Subarray Sums
"""

import heapq

class Solution:
    def rangeSum(self, nums, n, left, right):
        left -= 1
        right -= 1

        q = []

        for i in range(n):
            prefix = 0
            for j in range(i, n):
                prefix += nums[j]
                heapq.heappush(q, prefix)

        cnt = 0
        ans = 0
        while cnt < left:
            heapq.heappop(q)
            cnt += 1

        while cnt <= right:
            ans += heapq.heappop(q)
            cnt += 1

        return ans % 1_000_000_007
