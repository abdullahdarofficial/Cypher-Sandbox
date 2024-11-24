class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs = float("inf")

        for row in matrix:
            for element in row:
                total_sum += abs(element)
                if element < 0:
                    negative_count += 1
                min_abs = min(min_abs, abs(element))

        if negative_count % 2 == 1:
            return total_sum - 2 * min_abs
        else:
            return total_sum
        

            
        