"""
https://leetcode.com/problems/total-characters-in-string-after-transformations-i
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7

        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord("a")] += 1

        for _ in range(t):
            next_arr = [0] * 26
            next_arr[0] = arr[25]
            next_arr[1] = (arr[25] + arr[0]) % mod

            for i in range(2, 26):
                next_arr[i] = arr[i - 1]
            arr = next_arr
        return sum(arr) % mod