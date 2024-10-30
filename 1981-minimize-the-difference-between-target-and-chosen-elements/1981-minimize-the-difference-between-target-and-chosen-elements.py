class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Initialize the set of possible sums with the first row
        possible_sums = set()
    
    # Start with the sums from the first row
        for num in mat[0]:
            possible_sums.add(num)

    # Process each subsequent row
        for row in mat[1:]:
            new_sums = set()
            for num in row:
                for existing_sum in possible_sums:
                    new_sums.add(existing_sum + num)
            possible_sums = new_sums

    # Find the closest sum to the target
        closest_diff = float('inf')
        for s in possible_sums:
            closest_diff = min(closest_diff, abs(s - target))
    
        return closest_diff