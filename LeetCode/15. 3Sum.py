class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        n = len(nums)
        h = set()
        res = []
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    if (nums[i], nums[left], nums[right]) not in h:
                        h.add((nums[i], nums[left], nums[right]))
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1
        return res