class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # result = set()
        # def comb(curr):
        #     total = sum(curr)
        #     if total >= target:
        #         if total == target:
        #             curr.sort()
        #             result.add(tuple(curr))
        #     else:
        #         for num in candidates:
        #             comb(curr + [num])
        # comb([])
        # return [list(num) for num in result]

        # result = []
        # def comb(curr):
        #     total = sum(curr)
        #     if total >= target:
        #         if total == target:
        #             curr.sort()
        #             if curr not in result:
        #                 result.append(curr)
        #     else:
        #         for num in candidates:
        #             comb(curr + [num])
        # comb([])
        # return result



        result = []
        def backtrack(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                backtrack(i, curr + [candidates[i]], total + candidates[i])
        backtrack(0,[],0)
        return result