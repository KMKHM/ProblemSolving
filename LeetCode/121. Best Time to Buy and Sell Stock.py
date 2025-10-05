class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_min = 1e9

        for price in prices:
            res = max(price - cur_min, res)
            cur_min = min(cur_min, price)

        return res