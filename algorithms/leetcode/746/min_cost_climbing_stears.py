from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]
        for i in range(2, len(cost)):
            cost[i]+=min(cost[i-1], cost[i-2])
        return cost[i]