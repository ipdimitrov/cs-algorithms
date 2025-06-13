class Solution:
    def longestPalindrome(self, s: str) -> str:
        out, lenout = "", 0
        for i in range(len(s)):
            for j in range(0, min(i, len(s)-i)+1):
                st = s[i-j:i+1+j]
                if st != st[::-1]:
                    break
                if j*2+1 >lenout:
                    out = st
                    lenout = len(st)
        for i in range(len(s)):
            for j in range(1, min(i, len(s)-i)+1):
                st = s[i-j:i+j]
                if st != st[::-1]:
                    break
                if j*2 >lenout:
                    out = st
                    lenout = len(st)
        return out
