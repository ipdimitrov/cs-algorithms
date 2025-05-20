class Solution:
    def findDuplicate(self, nums) -> int:
        d = {}
        for num in nums:
            if d.get(num, False):
                return num
            d[num]=True