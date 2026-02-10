from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        even = set()
        odd = set()

        res = 0

        for j in range(n - 1):
            i = j + 1
            if nums[j] % 2:
                odd.add(nums[j])
            else:
                even.add(nums[j])
            while i < n:
                if nums[i] % 2:
                    odd.add(nums[i])
                else:
                    even.add(nums[i])

                if len(even) == len(odd):
                    res = max(res, i - j + 1)
                i += 1
            even, odd = set(), set()

        return res