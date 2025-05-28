from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        def dfs(index, items):
            out.append(items)
            for i in range(index, len(nums)):
                if i<=index or nums[i] != nums[i-1]:
                    dfs(i+1, items+[nums[i]])
        dfs(0, [])
        return out