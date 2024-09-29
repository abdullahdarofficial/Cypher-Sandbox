class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        currmax = max(candies)
        result = []
        for candie in candies:
            if candie + extraCandies >= currmax:
                result.append(True)
            else:
                result.append(False)
        return result