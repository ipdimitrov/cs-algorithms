from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0] * (n+1)
        for i in range(n+1):
            out[i] = out[i >> 1] + (i & 1)
        return out