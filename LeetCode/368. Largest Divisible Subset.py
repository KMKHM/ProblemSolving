"""
368. Largest Divisible Subset
문제: https://leetcode.com/problems/largest-divisible-subset/description/
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)

        if n == 1:
            return nums

        nums.sort()

        dp = [[i] for i in nums]

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)
