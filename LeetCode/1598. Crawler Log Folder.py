"""
1598. Crawler Log Folder
문제: https://leetcode.com/problems/crawler-log-folder/description/
"""
class Solution:
    def minOperations(self, logs):
        ans = 0

        for log in logs:
            if log == "../":
                if ans:
                    ans -= 1
            elif log == "./":
                continue
            else:
                ans += 1
        return ans

"""
class Solution {
    public int minOperations(String[] logs) {
        int ans = 0;

        for (String log:logs) {
            if (log.equals("../")) {
                if (ans != 0) {
                    ans -= 1;
                }
            } else if (log.equals("./")) {
                continue;
            } else {
                ans += 1;
            }
        }
        return ans;
    }
}
"""