from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        original_nums = nums.copy()
        x = [0 for _ in range(len(nums))]
        nums.sort()
        for i, num in enumerate(original_nums):
            x[i] = nums.index(num)
        return x

# nums = [8,1,2,2,3]
# print(Solution().smallerNumbersThanCurrent(nums))
