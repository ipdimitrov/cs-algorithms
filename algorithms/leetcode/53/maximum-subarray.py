from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = max(nums)
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum<0:
                curr_sum = 0
            else:
                curr_max = max(curr_max, curr_sum)
        return curr_max