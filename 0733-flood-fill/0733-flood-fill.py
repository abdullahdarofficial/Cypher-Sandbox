class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, no need to proceed
        if original_color == color:
            return image

        def check(i, j):
            # Check boundaries
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            # Only proceed if the current cell is the original color
            if image[i][j] == original_color:
                image[i][j] = color  # Fill the cell with the new color
                
                # Recursive calls for the neighboring cells
                check(i - 1, j)
                check(i + 1, j)
                check(i, j - 1)
                check(i, j + 1)

        # Start the fill from the given starting cell
        check(sr, sc)
        return image