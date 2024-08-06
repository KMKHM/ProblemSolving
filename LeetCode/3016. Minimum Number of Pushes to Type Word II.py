"""
3016. Minimum Number of Pushes to Type Word II
문제: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
"""
from collections import Counter

class Solution:
    def minimumPushes(self, word):
        res, cnt = 0, 0
        weight = 1
        dic = sorted(Counter(word).items(), reverse=True, key=lambda x:x[1])

        for i, j in dic:
            cnt += 1
            res += (j * weight)
            if cnt % 8 == 0:
                weight += 1

        return res

"""
class Solution {
    public int minimumPushes(String word) {
       int res = 0;
       int cnt = 0;
       int weight = 1;

       Map<Character, Integer> map = new HashMap<>();

       for (char c : word.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

       List<Integer> keys = new ArrayList<>(map.values());

       Collections.sort(keys);
       Collections.reverse(keys);
    
       for (int v : keys) {
            cnt++;
            res += (weight * v);
            if (cnt % 8 == 0) {
                weight++;
            }
       }

       return res;

    }
}
"""

"""
class Solution {
    public int minimumPushes(String word) {
        int[] arr = new int[26];

        for (char c : word.toCharArray()) {
            arr[c - 'a']++;
        }

        Arrays.sort(arr);

        
        int res = 0;
        int weight = 1;
        int cnt = 0;

        for (int i=25; i>=0; i--) {
            cnt++;
            res += (arr[i] * weight);
            if (cnt % 8 == 0){
                weight++;
            } 
        }

        return res; 

    }
}
"""

