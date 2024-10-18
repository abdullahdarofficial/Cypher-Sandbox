class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # n = len(cost)
        # result = []
        # def recursive(level, currcost):
        #     if level >= n:
        #         result.append(currcost)
        #     else:
        #         recursive(level + 1, currcost + cost[level])
        #         recursive(level + 2, currcost + cost[level])

        # recursive(0, 0)
        # recursive(1, 0)

        # return min(result)
            
        # dp 

        n = len(cost)
        arr = [0] * n
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost)

        arr[0] = cost[0]
        arr[1] = cost[1]
        for i in range(2, n ):
            arr[i] = cost[i] + min(arr[i - 1], arr[i - 2])

        return min(arr[-1] , arr[-2])
