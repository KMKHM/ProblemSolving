"""
1460. Make Two Arrays Equal by Reversing Subarrays
문제: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/
"""
class Solution:
    def canBeEqual(self, target, arr):
        tmp = [0] * 1001

        for i in range(len(target)):
            tmp[target[i]] += 1
            tmp[arr[i]] -= 1

        for num in tmp:
            if num:
                return False

        return True

"""
class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int[] tmp = new int[1001];


        for (int i=0; i<target.length; i++) {
            tmp[target[i]]++;
            tmp[arr[i]]--;
        }

        for (int i : tmp) {
            if (i > 0) return false;
        }
        
        return true;
    }
}
"""