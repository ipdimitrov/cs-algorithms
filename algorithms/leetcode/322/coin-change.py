from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        out = [0] + [amount+1]*(amount)
        for i in range(0, amount+1):
            for coin in coins:
                if i-coin>=0:
                    out[i] = min(out[i], out[i-coin] + 1)
        if out[amount] == amount+1:
            return -1
        return out[amount]