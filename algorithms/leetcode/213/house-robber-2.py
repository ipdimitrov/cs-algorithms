from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        nums_1 = [0]*len(nums)
        nums_0 = [0]*len(nums)
        nums_0[1] = nums[1]
        nums_1[0] = nums[0]
        if len(nums) > 2:
            nums_1[2] = nums[2] + nums_1[0]
            nums_0[2] = nums[2]
        for i in range (3, len(nums)):
            nums_1[i] = nums[i] + max(nums_1[i-2], nums_1[i-3])
            nums_0[i] = nums[i] + max(nums_0[i-2], nums_0[i-3])
        print(nums_1)
        print(nums_0)
        return max(nums_0[-1], nums_0[-2], nums_1[-2], nums_1[-1] - nums[-1], nums_1[-1] - nums[0])