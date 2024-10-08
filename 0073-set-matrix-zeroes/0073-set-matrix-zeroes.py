# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         def change_row_col(ai,aj):
#             m = len(matrix) #rows
#             n = len(matrix[0]) #cols

#             i = ai
#             j = aj

#             while i < m: #down
#                 if matrix[i][j] != 0 :
#                     matrix[i][j] = -1572
#                 i += 1

#             i = ai
#             j = aj

#             while i >= 0: #up
#                 if matrix[i][j] != 0:
#                     matrix[i][j] = -1572
#                 i-=1
                

#             i = ai
#             j = aj
#             while j < n: #right
#                 if matrix[i][j] != 0:
#                     matrix[i][j] = -1572
#                 j += 1
                
                
#             i = ai
#             j = aj
#             while j >= 0: #left
#                 if matrix[i][j] != 0:
#                     matrix[i][j] = -1572
#                 j-=1
                

#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     change_row_col(i,j)

#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == -1572:
#                     matrix[i][j] = 0

        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # Check if first row has any zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column has any zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
        
        # Use first row and column to mark zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark first column
                    matrix[0][j] = 0  # Mark first row
        
        # Zero out cells based on marks in first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
