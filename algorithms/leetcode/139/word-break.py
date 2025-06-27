from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(max(len(word) for word in wordDict), 20) + 1
        accessible = [False] * len(s)
        for i in range(len(s)):
            if not i or accessible[i]:
                if len(s)-i<21 and s[i:] in wordDict:
                    return True
                for j in range(i+1, min(i+max_len, len(s))):
                    if s[i:j] in wordDict:
                        accessible[j] = True
        return False