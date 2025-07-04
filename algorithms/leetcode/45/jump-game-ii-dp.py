from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_distance = [len(nums)]*(len(nums)-1)
        min_distance.append(0)
        for i in range (len(nums)-2,-1,-1):
            if nums[i]:
                min_distance[i] = min(min_distance[i+1:i+nums[i]+1]) + 1
        return min_distance[0]