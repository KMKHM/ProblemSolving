"""
Robot Return to Origin
문제: https://leetcode.com/problems/robot-return-to-origin/description/
"""

class Solution:
    def judgeCircle(self, moves):
        return moves.count("L")==moves.count("R") and moves.count("D")==moves.count("U")

"""
class Solution {
    public boolean judgeCircle(String moves) {
        int u=0, d=0, l=0, r=0;

        for (char m:moves.toCharArray()) {
            if (m=='U') {
                u++;
            } else if (m == 'D') {
                d++;
            } else if (m == 'L') {
                l++;
            } else {
                r++;
            }
        }

        return u == d && l == r;
    }
}
"""