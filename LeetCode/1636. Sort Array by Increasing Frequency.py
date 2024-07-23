"""
Sort Array by Increasing Frequency
문제: https://leetcode.com/problems/sort-array-by-increasing-frequency/description
"""

from collections import Counter

class Solution:
    def frequencySort(self, nums):
        dic = Counter(nums)
        return sorted(nums, key=lambda x: (dic[x], -x))


"""
class Solution {
    public int[] frequencySort(int[] nums) {
       Map<Integer, Integer> map = new HashMap<>();
       
       for (int i: nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
       }
       
       List<Integer> keys = new ArrayList(map.keySet());

       Collections.sort(keys, (a, b) -> map.get(a) == map.get(b) ? b-a:map.get(a)-map.get(b));
       
       int idx = 0;
       for (int i: keys) {
        for (int j=0; j<map.get(i); j++) {
            nums[idx++] = i;
        }
       }
       return nums;


    }
}
"""