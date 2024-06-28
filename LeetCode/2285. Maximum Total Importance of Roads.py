"""
Maximum Total Importance of Roads
문제: https://leetcode.com/problems/maximum-total-importance-of-roads/description/
"""


class Solution:
    def maximumImportance(self, n, roads):

        connect = [0] * n

        for a, b in roads:
            connect[a] += 1
            connect[b] += 1

        connect = sorted(enumerate(connect), key=lambda x: -x[1])

        weight = [0] * n

        for i, j in connect:
            weight[i] = n
            n -= 1

        ans = 0

        for a, b in roads:
            ans += (weight[a] + weight[b])

        return ans