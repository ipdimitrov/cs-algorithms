class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x <0:
            sign = -1
            x = -x
        y = 0
        while x:
            y = y*10 + x%10
            x//=10
        y*=sign
        if y<-2**31 or y>2**31-1:
            return 0
        return y