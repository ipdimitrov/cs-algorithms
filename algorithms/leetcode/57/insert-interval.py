from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                out.append(intervals[i])
            elif intervals[i][0]>newInterval[1]:
                out.append(newInterval)
                return out + intervals[i:]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]),
                               max(intervals[i][1], newInterval[1])]
        out.append(newInterval)
        return out