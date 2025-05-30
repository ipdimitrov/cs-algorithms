from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs","8": "tuv", "9": "wxyz"}
        if digits is "":
            return []
        out = [""]
        for digit in digits:
            out = [el + i for i in d[digit] for el in out]
        return out