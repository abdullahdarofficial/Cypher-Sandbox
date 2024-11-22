class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, curr_sum, path):
            if curr_sum == target:
                result.append(path[:])
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    if curr_sum + candidates[i] > target:
                        break
                    path.append(candidates[i])
                    backtrack(i + 1, curr_sum + candidates[i], path)
                    path.pop()
        backtrack(0,0,[])
        return result