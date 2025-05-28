from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        leng = len(candidates)
        def dfs(index, tar, curr_list):
            prev = 0
            for i in range (index, leng):
                if candidates[i] == prev:
                    continue
                tar_local = tar - candidates[i]
                if tar_local<0:
                    return
                if tar_local==0:
                    output.append(curr_list + [candidates[i]])
                    return
                dfs(i+1, tar_local, curr_list + [candidates[i]])
                prev = candidates[i]
        dfs(0, target, [])
        return output
