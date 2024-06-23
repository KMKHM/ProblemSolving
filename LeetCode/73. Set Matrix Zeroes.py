"""
Set Matrix Zeroes
문제: https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])

        col_set, row_set = set(), set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    col_set.add(i)
                    row_set.add(j)

        for col in col_set:
            for j in range(m):
                matrix[col][j] = 0

        for i in range(n):
            for row in row_set:
                matrix[i][row] = 0