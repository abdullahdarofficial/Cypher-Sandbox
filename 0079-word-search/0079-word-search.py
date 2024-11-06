class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def backtrack(index: int, x: int, y: int, visited: Set[Tuple[int, int]]) -> bool:
            if index == len(word):
                return True
            
            if not (0 <= x < n and 0 <= y < m) or (x, y) in visited or board[x][y] != word[index]:
                return False
            
            visited.add((x, y))
            # Recursively search in all four directions
            found = (
                backtrack(index + 1, x + 1, y, visited) or
                backtrack(index + 1, x - 1, y, visited) or
                backtrack(index + 1, x, y + 1, visited) or
                backtrack(index + 1, x, y - 1, visited)
            )
            visited.remove((x, y))  # Backtrack
            
            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and backtrack(0, i, j, set()):
                    return True  # Early return if word is found
        return False
