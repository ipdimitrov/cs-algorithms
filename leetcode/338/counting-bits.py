from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        n_copy = n + 1
        out = [0]
        while n:
            out = out + [i+1 for i in out]
            n>>=1
        return out[:n_copy]