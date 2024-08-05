"""
2053. Kth Distinct String in an Array
문제: https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
"""

from collections import Counter

class Solution:
    def kthDistinct(self, arr, k):
        dic = Counter(arr)
        for i, j in dic.items():
            if j == 1:
                k -= 1
                if k == 0:
                    return i
        return ""

"""
class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> map = new LinkedHashMap<>();

        for (String s : arr) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }

        for (String key: map.keySet()) {
            if (map.get(key) == 1) {
                k--;
                if (k == 0) {
                    return key;
                }
            }
        }
        return "";
    }
}
"""