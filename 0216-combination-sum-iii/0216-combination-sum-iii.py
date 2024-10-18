class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []

        def backtrack(currsum, currele, start):
            if len(currele) == k:
                if currsum == n:
                    result.append(currele)
                return 

            for num in range(start, 10):
                if currsum + num <= n:
                    backtrack(currsum + num, currele + [num], num + 1)
    
        backtrack(0, [], 1)
        return result