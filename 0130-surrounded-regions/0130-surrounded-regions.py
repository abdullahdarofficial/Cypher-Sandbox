class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_bordered(i, j, visited):
            
            if i < 0 or j < 0 or i == n or j == m:
                return False
            if (i , j) in visited:
                return False
            visited.add((i,j))
            if board[i][j] == "X":
                return False
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                return True
            return (is_bordered(i, j - 1, visited) or 
                    is_bordered(i, j + 1, visited) or 
                    is_bordered(i - 1, j, visited) or 
                    is_bordered(i + 1, j, visited))

        def capture_it(i, j, visited):
            
            if i < 0 or j < 0 or i == n or j == m:
                return 
            if (i , j) in visited:
                return False
                
            visited.add((i,j))

            if board[i][j] == "O":
                board[i][j] = "X"
                capture_it(i, j - 1, visited)
                capture_it(i, j + 1, visited)
                capture_it(i - 1, j, visited)
                capture_it(i + 1, j, visited)

        n = len(board)
        m = len(board[0]) if n > 0 else 0

        visited = set()

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    visited = set()
                    if not is_bordered(i, j, visited):
                        capture = set()
                        capture_it(i, j, capture)