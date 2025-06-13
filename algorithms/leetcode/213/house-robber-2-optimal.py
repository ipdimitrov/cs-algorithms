from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robone(nums: List[int]) -> int:
            before_1, before_2 = 0, 0
            for num in nums:
                before_1, before_2 = max(num + before_2, before_1), before_1
            return before_1
        return max(robone(nums[:-1]), robone(nums[1:]))