from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        before_1, before_2 = 0, 0
        for num in nums:
            before_1, before_2 = max(num + before_2, before_1), before_1
        return before_1