"""
Average Waiting Time
문제: https://leetcode.com/problems/average-waiting-time/description/
"""


class Solution:
    def averageWaitingTime(self, customers):
        start = 0
        wait = 0

        for arrive, time in customers:
            start = max(start, arrive) + time
            wait += (start - arrive)

        return wait / len(customers)

"""
class Solution {
    public double averageWaitingTime(int[][] customers) {
        long wait = 0, start = 0;

        for (int[] arr:customers) {
            start = Math.max(arr[0], start) + arr[1];
            wait += start - arr[0];
        }

        return (double) wait/customers.length;
    }
}
"""