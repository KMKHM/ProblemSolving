"""
1518. Water Bottles
문제: https://leetcode.com/problems/water-bottles/description/
"""

class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        ans = numBottles

        while numBottles >= numExchange:
            ans += (numBottles // numExchange)
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return ans