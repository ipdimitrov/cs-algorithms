class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range (32):
            out = (out<<1) + (n%2)
            n>>=1
        return out