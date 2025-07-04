from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        access = [False]*(len(nums)-1)
        access.append(True)
        for i in range (len(nums)-1, -1, -1):
            if True in access[i+1:i+1+nums[i]]:
                access[i]=True
        return access[0]