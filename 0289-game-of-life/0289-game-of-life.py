class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        matrix = board
        
        def game(matrix):
            n = len(matrix)

            def count_neighbours(x, y):
                direction = [(-1, -1), (-1, 0), (-1, 1),
                             (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                live = 0
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        if matrix[nx][ny] == 1 or matrix[nx][ny] == 4:
                            live += 1
                return live

            # First pass: Mark cells with temporary states (3 and 4)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    live_neighbors = count_neighbours(i, j)

                    if matrix[i][j] == 1:  # Live cell
                        if live_neighbors < 2 or live_neighbors > 3:
                            matrix[i][j] = 4  # Live to dead
                    elif matrix[i][j] == 0:  # Dead cell
                        if live_neighbors == 3:
                            matrix[i][j] = 3  # Dead to live

            # Second pass: Update the matrix based on temporary states
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 3:
                        matrix[i][j] = 1  # Dead to live
                    elif matrix[i][j] == 4:
                        matrix[i][j] = 0  # Live to dead

        game(matrix)
