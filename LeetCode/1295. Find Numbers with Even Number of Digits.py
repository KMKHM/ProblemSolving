"""
문제: https://leetcode.com/problems/find-numbers-with-even-number-of-digits
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for num in nums if not len(str(num)) % 2])