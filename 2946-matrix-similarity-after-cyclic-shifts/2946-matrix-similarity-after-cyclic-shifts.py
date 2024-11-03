class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        # copy = [row for row in mat]
        # k %= len(mat)
        # for _ in range(k):
        #     for index, row in enumerate(copy):
        #         if index & 1 == 1:
        #             # odd
        #             ele = row[-1]
        #             i = len(row) - 1
        #             while i > 0:
        #                 row[i] = row[i - 1]
        #                 i -= 1
        #             row[0] = ele
        #         else:
        #             # even
        #             ele = row[0]
        #             i = 0
        #             while i < len(row) - 1:
        #                 row[i] = row[i + 1]
        #             row[-1] = ele
        # return copy == mat

        n = len(mat)
        m = len(mat[0])
        k %= m
        transformed = [[0] * m for _ in range(n)]
        for i in range(n):
            if i % 2 == 0:
                transformed[i] = mat[i][-k:] + mat[i][:-k]
            else:
                transformed[i] = mat[i][k:] + mat[i][:k]
        return transformed == mat
