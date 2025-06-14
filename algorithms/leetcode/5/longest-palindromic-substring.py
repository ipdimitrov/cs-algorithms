class Solution:
    def longestPalindrome(self, s: str) -> str:
        out, lenout = s[0], 1
        for i in range(1, len(s)):
            if lenout >= (len(s)-i)*2:
                break
            for j in range(1, min(i, len(s)-i-1)+1):
                if s[i-j] != s[i+j]:
                    break
                if j*2+1 >lenout:
                    out = s[i-j:i+1+j]
                    lenout = j*2+1
            for j in range(1, min(i, len(s)-i)+1):
                if s[i-j] != s[i+j-1]:
                    break
                if j*2 >lenout:
                    out = s[i-j:i+j]
                    lenout = j*2
        return out
