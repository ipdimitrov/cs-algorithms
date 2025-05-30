from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def iterate(nums, curr_list):
            if len(nums) == 1:
                permutations.append(curr_list + nums)
            else:
                for i in range(len(nums)):
                    iterate(nums[:i] + nums[i+1:], curr_list + [nums[i]])
        iterate(nums, [])
        return permutations