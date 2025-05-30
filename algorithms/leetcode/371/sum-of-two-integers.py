class Solution:
    def getSum(self, a: int, b: int) -> int:
        out, rest = 0, 0
        for i in range(32):
            out = ((rest^(a&1)^(b&1))<<i) | out
            rest = ((a&1) + (b&1) + rest) > 1
            a>>=1
            b>>=1
        if out > (2**31-1): # this could be done with 0x7FFFFFFF to avoid minus
            return ~(out ^(2**32))
        return out