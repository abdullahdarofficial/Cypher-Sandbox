class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        combined = sorted(zip(dist, speed), key = lambda x : x[0]/x[1])
        dist_sorted, speed_sorted = zip(*combined)
        dist = list(dist_sorted)
        speed = list(speed_sorted)

        n = len(speed)
        count = 1
        for i in range(1, n):
            if (dist[i] - (i * speed[i])) > 0:
                count += 1
            else:
                return count
        return count



