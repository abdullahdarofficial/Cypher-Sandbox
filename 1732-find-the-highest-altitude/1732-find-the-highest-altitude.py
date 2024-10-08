class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        maxalt = 0
        currg = 0
        for g in gain:
            currg += g
            maxalt = max(maxalt, currg)
        return maxalt