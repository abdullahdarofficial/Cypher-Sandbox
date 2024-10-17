class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # maxbananas = max(piles)
        # minbananas = min(piles)
        # minnumber = 0
        # for num in range(minbananas, maxbananas):
        #     totalcount = 0
        #     print(piles)
        #     for pile in piles:
        #         count = 0
        #         while pile >=0:
        #             count += 1
        #             pile = pile // num
        #         totalcount += count
        #     if totalcount <= h:
        #         minnumber = min(minnumber, totalcount)
                

        # return minnumber

        def canFinish(speed):
            totalhours = 0
            for pile in piles:
                totalhours += (pile + speed - 1) // speed
            return totalhours <= h

        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return left

