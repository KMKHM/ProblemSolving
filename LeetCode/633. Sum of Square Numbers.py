"""
Sum of Square Numbers
문제: https://leetcode.com/problems/sum-of-square-numbers/description/
"""
class Solution:
    def judgeSquareSum(self, c):
        left, right = 0, int(c**0.5)

        while left <= right:
            cur = left ** 2 + right ** 2

            if cur == c:
                return True

            if cur < c:
                left += 1
            else:
                right += 1
        return False

a = Solution()