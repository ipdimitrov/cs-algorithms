from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range (1, len(intervals)):
            if end<intervals[i][0]:
                out.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        out.append([start, end])
        return out