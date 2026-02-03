from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        n = len(nums)

        if n < 4:
            return False

        increase = decrease = last_increase = False

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            """
            증가하는 경우
            1. 앞에서 증가하고 뒷 부분 체크안하면 increase=True
            2. 감소하는 부분 지나고 증가하면 last_increase=True
            감소하는 경우
            1. 앞에서 증가 부분 후 감소하는 경우에는 감소하는 부분 만족
            2. 마지막 증가하는 부분이 True인데 감소하는 경우 만족 X
            3. 첫 번째 부터 감소하면 바로 False
            """
            if nums[i] > nums[i-1]: # 증가하는 경우
                if not decrease and not last_increase: # 첫 번째 증가부분
                    increase = True
                elif decrease: # 마지막 증가부분
                    last_increase = True
            elif nums[i] < nums[i-1]: # 감소하는 경우
                if not increase:
                    return False

                elif increase and not last_increase:
                    decrease = True

                elif last_increase: # 마지막 증가 부분에서 감소하는 경우
                    return False
        return increase and decrease and last_increase