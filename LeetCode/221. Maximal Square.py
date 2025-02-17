"""
Maximal Square
문제: https://leetcode.com/problems/maximal-square/description/
"""


class Solution:
    def maximalSquare(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        if n == 0:
            return 0

        # DynamicProgramming 테이블
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        val = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    val = max(val, dp[i][j])

        return val * val





