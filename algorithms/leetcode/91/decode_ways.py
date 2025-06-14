class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=="0":
            return 0
        next_1, next_2 = 0, 1
        if s[len(s)-1]!="0":
            next_1 = 1
        for i in range (len(s)-2, -1, -1):
            if s[i]=="0":
                next_1, next_2 = 0, next_1
            elif s[i:i+2]<"27":
                next_1, next_2 = next_1+next_2, next_1
            else:
                next_2 = next_1
        return next_1