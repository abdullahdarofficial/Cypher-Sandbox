class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 1:
            return True
        
        for i in range(1, len(coordinates) - 1):
            first , second = coordinates[i - 1], coordinates[i] 

            if (second[0] - first[0]) == 0:
                return False
                
            if (second[1] - first[1])/(second[0] - first[0]) != 1:
                return False
        return True