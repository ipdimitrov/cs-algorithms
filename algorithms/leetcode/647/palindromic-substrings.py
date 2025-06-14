class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 1
        for i in range(1, len(s)):
            for j in range(0, min(i, len(s)-i-1)+1):
                if s[i-j] != s[i+j]:
                    break
                out+=1
            for j in range(1, min(i, len(s)-i)+1):
                if s[i-j] != s[i+j-1]:
                    break
                out+=1
        return out