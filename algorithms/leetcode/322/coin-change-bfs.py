from typing import List
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        q = deque([0])
        seen = [True] + [False] * (amount)
        level = 0
        while q:
            level +=1
            for _ in range (len(q)):
                curr = q.popleft()
                for coin in coins:
                    next_coin = curr + coin
                    if next_coin == amount:
                        return level
                    if next_coin<amount and seen[next_coin]==False:
                        seen[next_coin]=True
                        q.append(next_coin)
        return -1