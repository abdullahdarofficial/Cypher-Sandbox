class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtracking(start, end, curr):
            print(curr)
            if len(curr) == k:
                result.append(curr)
                return
            for i in range(start, end + 1):
                backtracking(i + 1, end, curr + [i])
        backtracking(1,n,[])
        return result

        
            