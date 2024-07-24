"""
Sort the Jumbled Numbers
문제: https://leetcode.com/problems/sort-the-jumbled-numbers/description/
"""

from collections import Counter

class Solution:
    def sortJumbled(self, mapping, nums):
        dic = Counter()

        for i in range(10):
            dic[str(i)] = str(mapping[i])

        tmp = Counter(nums)

        for i, j in tmp.items():
            s = str(i)
            a = ""
            for c in s:
                a += dic[c]
            tmp[i] = int(a)

        return sorted(nums, key=lambda x: tmp[x])

"""
class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        Map<Character, Character> map = new HashMap<>();
        Integer[] arr = new Integer[nums.length];

        for (int i=0; i<nums.length; i++) {
            arr[i] = nums[i];
        }

        for (int i=0; i<10; i++) {
            map.put(Character.forDigit(i, 10), Character.forDigit(mapping[i], 10));
        }

        Map<Integer, Integer> tmp = new HashMap<>();

        for (int num : nums) {
            StringBuilder s = new StringBuilder();
            for (char c : String.valueOf(num).toCharArray()) {
                s.append(map.get(c));
            }
            tmp.put(num, Integer.valueOf(s.toString()));
        }

        
        Arrays.sort(arr, (a, b) -> tmp.get(a) - tmp.get(b));
        for (int i=0; i<nums.length; i++) {
            nums[i] = arr[i];
        }
        
        return nums;
    }
}
"""