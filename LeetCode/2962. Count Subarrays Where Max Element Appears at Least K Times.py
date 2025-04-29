"""
문제: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = i = cnt = 0
        val = max(nums)

        for j in range(len(nums)):
            if nums[j] == val:
                cnt += 1
            while cnt >= k:
                if nums[i] == val:
                    cnt -= 1
                i += 1
            res += i
        return res