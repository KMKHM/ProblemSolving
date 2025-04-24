from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        k = len(set(nums))
        res = i = 0

        dic = Counter()  # 현재 윈도우에 있는 요소들의 빈도를 저장

        for j in range(n):
            dic[nums[j]] += 1  # 현재 요소를 윈도우에 추가

            """
            윈도우에 있는 서로 다른 요소의 개수가 k와 같아지면
            시작점을 오른쪽으로 이동시켜 최소한의 complete 부분 배열을 찾음
            """
            while len(dic) == k:
                dic[nums[i]] -= 1
                if dic[nums[i]] == 0:
                    del dic[nums[i]]  # 빈도가 0이 되면 딕셔너리에서 제거
                i += 1
            # i는 현재까지 발견된 complete 부분 배열의 개수를 더함
            res += i

        return res