class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # def printit():
        #     for row in matrix:
        #         print(row)
        #     print()
        # m = 0
        # n = len(matrix)
        # if n % 2 != 0:
        #     n += 1
        # else:
        #     m = 1
        # n //= 2
        # end = len(matrix) - 1
        # count = 0
        # print(n,m)
        # for i in range(n):
        #     for j in range(i, n + m - i):
        #         print(i,j)
        #         print("before", count)
        #         printit()
        #         matrix[j][end - i], matrix[end - i][end - j], matrix[end - j][i], matrix[i][j] = matrix[i][j], matrix[j][end - i], matrix[end - i][end - j], matrix[end - j][i]
        #         print("after", count)
        #         count += 1
        #         printit()


        n = len(matrix)

        # transpose of matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for row in matrix:
            row.reverse()

        