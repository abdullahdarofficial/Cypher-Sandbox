class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points.sort(key = lambda s : s[1])

        arrows = 1
        _, old_xe = points[0]

        for i in range(1, len(points)):
            new_xs, new_xe = points[i]
            if new_xs > old_xe:
                arrows += 1
                old_xe = new_xe
            
        return arrows