from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def search(cand, target, curr_list):
            for i in range(len(cand)):
                if cand[i] < target:
                    search(cand[i:], target-cand[i], curr_list+[cand[i]])
                elif cand[i] == target:
                    combinations.append(curr_list+[cand[i]])
        search(candidates, target, [])
        return combinations