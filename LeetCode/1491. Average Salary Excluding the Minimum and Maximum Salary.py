"""
Average Salary Excluding the Minimum and Maximum Salary
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""

class Solution:
    def average(self, salary):
        salary.sort()
        return sum(salary[i] for i in range(1, len(salary)-1)) / (len(salary) - 2)


"""
class Solution {
    public double average(int[] salary) {
        Arrays.sort(salary);
        long tmp = 0;

        for (int i=1; i<salary.length-1; i++) {
            tmp += salary[i];
        }

        return (double) tmp / (salary.length - 2);
    }
}
"""