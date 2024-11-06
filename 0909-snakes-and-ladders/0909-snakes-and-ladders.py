
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n * n  # The last square number
        visited = [False] * (n2 + 1)  # To track visited squares
        queue = deque([(1, 0)])  # (current square, number of moves)

        while queue:
            curr_square, moves = queue.popleft()

            # If we reached the last square, return the number of moves
            if curr_square == n2:
                return moves

            # Try all possible dice rolls (1 to 6)
            for dice_roll in range(1, 7):
                next_square = curr_square + dice_roll

                if next_square <= n2 and not visited[next_square]:
                    visited[next_square] = True

                    # Check if there's a snake or ladder at next_square
                    row, col = self.get_position(next_square, n)
                    if board[row][col] != -1:
                        next_square = board[row][col]  # Follow the snake/ladder

                    # Add the destination square to the queue
                    queue.append((next_square, moves + 1))

        return -1  # If no solution is found

    def get_position(self, square: int, n: int) -> (int, int):
        # Convert 1D square number to row and column in the board
        square -= 1  # Convert to 0-indexed
        row = n - 1 - square // n  # row is counted from the bottom
        col = square % n
        if (n - 1 - row) % 2 == 1:
            col = n - 1 - col  # Reverse the column index for odd rows
        return row, col