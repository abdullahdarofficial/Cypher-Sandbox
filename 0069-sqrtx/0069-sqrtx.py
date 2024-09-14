# class Solution:
#     def mySqrt(self, x: int) -> int:
        
#         i = 1
#         while i <= x:

#             if (i * i) >= x:
#                 if (i * i) == x:
#                     return i
#                 return i - 1
#             i += 1
#         return 0


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 2, x // 2

        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid

            if mid_sq == x:
                return mid
            elif mid_sq < x:
                low = mid + 1
            else:
                high = mid - 1

        return high
